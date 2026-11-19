# Santa 2026 Kaggle release

This repository holds the release workflow, exact replay verifier, and encrypted
competition candidate. The workflow decrypts the candidate on the runner,
checks all 1,000 official puzzle IDs and the instruction count, and compares
the reported Kaggle score after an explicit publish dispatch.

The `kaggle-santa-2026` environment needs `SANTA_CANDIDATE_KEY` and
`KAGGLE_API_TOKEN`. Keep both in GitHub Actions secrets.

For the baseline release, use `artifacts/santa-2026.csv.enc`, score `137713`,
and SHA-256 `d02939b1ecc1c72ca50361bc889dd6300e9848de2d0cfb434106b81f8d8d459b`.

Baseline programs combine public releases from Hanif, Asterios, and Rudolph.

The refreshed candidate is `artifacts/santa-2026-137711.csv.enc`, score
`137711`, and SHA-256
`aca19423be5ad2a335ff3e93cc156fcafb845f4d2953e4448650bcc581d9dd77`.
The two additional savings are from the Apache-2.0
[Asterios program dataset](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments).

The previous verified candidate is `artifacts/santa-2026-137710.csv.enc`, score
`137710`, and SHA-256
`2b78949fbac45e0f1f39f6c6b55f505e78b10c7a77b3cd72ff7e1d3ad81bbbc5`.
The one-instruction saving comes from sharing a signed sum on `scored_0610`.

The previous verified candidate is `artifacts/santa-2026-136838.csv.enc`, score
`136838`, and SHA-256
`0590e3a52bd0c46517cb88ae1d68cb28fb56393a359bad5a0c9b2bba86d7664d`.
It merges shorter programs from version 51 of the
[Asterios program dataset](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments)
with the previous candidate. Native C rewrites then shorten 51 more programs.
The source dataset carries its own upstream attribution in `public_lineage.csv`.
The Apache-2.0 terms for the imported programs are in
[licenses/Apache-2.0.txt](licenses/Apache-2.0.txt).

The current verified candidate is `artifacts/santa-2026-136739.csv.enc`, score
`136739`, and SHA-256
`0cb33e18972b270bae7798ced44bbd861e304c7728695637f18c17cf5630aefa`.
It uses native Mojo and C group rewrites and merges public programs from
[Roman Rozen’s IceFire Strong Start v63](https://www.kaggle.com/code/romanrozen/santa-2026-icefire-strong-start?scriptVersionId=371584899)
and [Asterios Panoras’s program dataset v52](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments).
