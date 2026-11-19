"""Verify a frozen Santa 2026 candidate and optionally upload it."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory

COMPETITION = "santa-2026"
PUZZLES_SHA256 = "b0c70d849eca078a0e1cf9a4f7b47fd40b7435663f6f84de6725f84724500428"
KAGGLE = ["uvx", "--with", "six", "kaggle@2.2.5"]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def csv_reader(data):
    return csv.DictReader(io.StringIO(data.decode("utf-8"), newline=""), strict=True)


def replay_program(row, source):
    program = json.loads(source)
    if not isinstance(program, list) or len(program) > 4096:
        raise ValueError("program must contain at most 4096 instructions")
    count = int(row["registers"])
    limit = int(row["value_limit"])
    starts = json.loads(row["starting_values"])
    targets = set(json.loads(row["targets"]))
    registers = starts + [0] * (count - len(starts))
    hit = set(starts)
    for instruction in program:
        if not isinstance(instruction, list) or len(instruction) != 4:
            raise ValueError("invalid instruction shape")
        op, a, b, dest = instruction
        if any(type(r) is not int or not 0 <= r < count for r in (a, b, dest)):
            raise ValueError("invalid register index")
        left, right = registers[a], registers[b]
        if not left or not right:
            raise ValueError("read of an uninitialized register")
        if op == "+":
            value = left + right
        elif op == "-":
            value = left - right
        elif op == "*":
            value = left * right
        elif op == "/" and left % right == 0:
            value = left // right
        else:
            raise ValueError("invalid operator or inexact division")
        if not 0 < value <= limit:
            raise ValueError("result violates the puzzle value limit")
        registers[dest] = value
        hit.add(value)
    if not targets <= hit:
        raise ValueError("program missed a target")
    return len(program)


def inspect(puzzles_data, candidate_data, jobs):
    if sha256(puzzles_data) != PUZZLES_SHA256:
        raise ValueError("puzzles.csv differs from the pinned official file")
    puzzles = {row["id"]: row for row in csv_reader(puzzles_data)}
    if len(puzzles) != 1000:
        raise ValueError("expected 1,000 official puzzle IDs")
    rows = csv_reader(candidate_data)
    if rows.fieldnames != ["id", "program"]:
        raise ValueError("expected exactly the id,program columns")
    candidate = {}
    for row in rows:
        identifier = row["id"]
        if identifier in candidate or identifier not in puzzles or None in row or row["program"] is None:
            raise ValueError(f"unexpected, duplicate, or malformed row: {identifier!r}")
        candidate[identifier] = row["program"]
    if candidate.keys() != puzzles.keys():
        raise ValueError("candidate does not contain all 1,000 official puzzle IDs")

    def validate(item):
        identifier, program = item
        row = puzzles[identifier]
        if len(program.encode("utf-8")) > 131072:
            raise ValueError(f"{identifier} exceeds the program byte limit")
        try:
            return replay_program(row, program)
        except ValueError as error:
            raise ValueError(f"exact replay rejected {identifier}: {error}") from error

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        score = sum(pool.map(validate, candidate.items()))
    return {
        "competition": COMPETITION,
        "puzzles": len(candidate),
        "score": score,
        "sha256": sha256(candidate_data),
        "puzzles_sha256": PUZZLES_SHA256,
    }


def same_score(remote, expected):
    try:
        return Decimal(remote) == expected
    except (InvalidOperation, TypeError):
        return False


def publish(frozen, manifest, message, receipt_path):
    preflight = subprocess.run(
        [*KAGGLE, "competitions", "submissions", COMPETITION, "--page-size", "100", "--format", "json"],
        stdout=subprocess.PIPE, text=True,
    )
    if preflight.returncode:
        raise ValueError("Kaggle preflight failed before upload.")
    try:
        text = preflight.stdout.strip()
        recent = [] if text == "No submissions found" else json.loads(text)
        if not isinstance(recent, list):
            raise ValueError("expected a list")
    except ValueError as error:
        raise ValueError("Could not read Kaggle submission history. Upload stopped.") from error

    receipt = {"submission_ref": None, "remote_score": None, "sha256": manifest["sha256"],
               "local_score": manifest["score"], "status": "pending"}

    def save_receipt():
        if receipt_path:
            receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    digest = manifest["sha256"]
    score = manifest["score"]
    for previous in recent:
        description = previous.get("description") or ""
        if not description.endswith((f" ({score}, {digest})", f" ({score}, {digest[:12]})")):
            continue
        receipt["submission_ref"] = previous.get("ref")
        receipt["remote_score"] = previous.get("publicScore")
        receipt["reused"] = True
        if previous.get("status") == "SubmissionStatus.COMPLETE" and same_score(receipt["remote_score"], score):
            receipt["status"] = "verified"
            save_receipt()
            print(f"Existing verified Kaggle submission: {receipt['submission_ref']}")
            return
        receipt["status"] = "existing_submission_unconfirmed"
        save_receipt()
        raise ValueError("Kaggle already has a submission for this candidate. Check its status before retrying.")

    with TemporaryDirectory(prefix="santa-2026-") as temp:
        snapshot = Path(temp) / "submission.csv"
        snapshot.write_bytes(frozen)
        note = f"{message} ({score}, {digest})"
        command = [*KAGGLE, "competitions", "submit", COMPETITION, "-f", str(snapshot),
                   "-m", note, "--wait", "600"]
        with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as attempt:
            for line in attempt.stdout:
                print(line, end="", flush=True)
                ref = re.fullmatch(r"Submission ref: (\d+)\s*", line)
                if ref:
                    receipt["submission_ref"] = int(ref[1])
                    save_receipt()
                scored = re.fullmatch(r"Submission scored\. Public score: (.+?)\s*", line)
                if scored:
                    receipt["remote_score"] = scored[1]
            returncode = attempt.wait()

    validated = same_score(receipt["remote_score"], score)
    if returncode or receipt["submission_ref"] is None:
        receipt["status"] = "unconfirmed"
    elif not validated:
        receipt["status"] = "score_unconfirmed_or_mismatched"
    else:
        receipt["status"] = "verified"
    save_receipt()
    if receipt["status"] != "verified":
        raise ValueError("Kaggle did not confirm the expected score. Check submissions before retrying.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("puzzles", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--expect-score", required=True, type=int)
    parser.add_argument("--expect-sha256", required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--jobs", type=int, default=6)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--message", default="Verified Mojo/C portfolio")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-fA-F]{64}", args.expect_sha256):
        parser.error("--expect-sha256 must be a SHA-256 hex digest")
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    paths = [path.resolve() for path in (args.puzzles, args.candidate, args.manifest, args.receipt) if path]
    if len(paths) != len(set(paths)):
        parser.error("inputs, manifest, and receipt must use distinct paths")
    if args.receipt and not args.publish:
        parser.error("--receipt requires --publish")

    csv.field_size_limit(1 << 20)
    frozen = args.candidate.read_bytes()
    if sha256(frozen) != args.expect_sha256.lower():
        parser.error("candidate SHA-256 differs from the requested digest")
    try:
        manifest = inspect(args.puzzles.read_bytes(), frozen, args.jobs)
    except ValueError as error:
        parser.error(str(error))
    if manifest["score"] != args.expect_score:
        parser.error(f"expected score {args.expect_score}, replay found {manifest['score']}")
    report = json.dumps(manifest, indent=2) + "\n"
    if args.manifest:
        args.manifest.write_text(report, encoding="utf-8")
    print(report, end="", flush=True)

    if args.publish:
        try:
            publish(frozen, manifest, args.message, args.receipt)
        except ValueError as error:
            parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
