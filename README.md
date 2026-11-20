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

The previous verified candidate is `artifacts/santa-2026-136739.csv.enc`, score
`136739`, and SHA-256
`0cb33e18972b270bae7798ced44bbd861e304c7728695637f18c17cf5630aefa`.
It uses native Mojo and C group rewrites and merges public programs from
[Roman Rozen’s IceFire Strong Start v63](https://www.kaggle.com/code/romanrozen/santa-2026-icefire-strong-start?scriptVersionId=371584899)
and [Asterios Panoras’s program dataset v52](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments).

The previous verified candidate is `artifacts/santa-2026-136703.csv.enc`, score
`136703`, and SHA-256
`98933fb5d34eef0e08a7738ee6dc18e1b530fce4e30990bb24f76eba4450e439`.
It includes exact factor and shared-scale rewrites in C, shared-scaffold rewrites
in Mojo, and shorter recipes selected jointly from previously attributed traces.

The previous verified candidate is `artifacts/santa-2026-136666.csv.enc`, score
`136666`, and SHA-256
`c99bf8ebe3603d6ed5c329be46f876bdfc8d1301c75654e7038bb3b3ee46e12b`.
It includes shorter programs from
[Hanif Noer Rofiq’s public program bank v19](https://www.kaggle.com/datasets/hanifnoerrofiq/santa-2026-elf-calculator-peephole-programs/versions/19)
and further native group rewrites. The public bank’s author and upstream credits
are preserved in [its original notice](notices/hanif-v19.md).

The previous verified candidate is `artifacts/santa-2026-136650.csv.enc`, score
`136650`, and SHA-256
`ad91d46596e2bfc532e34b238355c5d455186fc5a32a01053313f9b7882cc3b9`.
It combines wider C factor searches, cross-trace rewrites, and shorter programs
from [Asterios catalog v55](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments/versions/55).
The public bank and selected puzzle credits are in the
[Asterios notice](notices/asterios-v55.md).

The previous verified candidate is `artifacts/santa-2026-136642.csv.enc`, score
`136642`, and SHA-256
`a1b482c566e094da3658957365e727e657320e46c16bedd3093a842ee2dd27bb`.
It adds C fan-out and Mojo DAG-join rewrites and shorter programs from the
Asterios public bank. Selected puzzle credits are recorded in the
[catalog v56 notice](notices/asterios-v56.md) and [catalog v57 notice](notices/asterios-v57.md).

The previous verified candidate is `artifacts/santa-2026-136636.csv.enc`, score
`136636`, and SHA-256
`8658eacaca8248c3973478cd5b1cef51a21e31faefd95c4cce97d34279a55f0d`.
It combines recipes across multiple traces with a shorter program from
[Asterios catalog v58](https://www.kaggle.com/datasets/asteriospanoras/santa-2026-elf-programs-and-experiments/versions/58).
The selected puzzle credit is in the [catalog v58 notice](notices/asterios-v58.md).

The previous verified candidate is `artifacts/santa-2026-136606.csv.enc`, score
`136606`, and SHA-256
`1c733c5f9c30c1291b203b591143e8c700cab9e9ace027a264374793b4c5866b`.
It adds native C recipe selection and shorter programs from the Asterios
public bank. Selected puzzle IDs are recorded in the
[catalog v59 notice](notices/asterios-v59.md).

The previous verified candidate is `artifacts/santa-2026-136599.csv.enc`, score
`136599`, and SHA-256
`900f802c4b90223800d1ab5a5e75bc50b143028b64aaf6d5db7148c8b295d291`.
It adds C searches that factor signed relations between roots, a Mojo
search for shared two-operation radices, and shorter programs from
[Asterios catalog v60](notices/asterios-v60.md).

The previous verified candidate is `artifacts/santa-2026-136589.csv.enc`, score
`136589`, and SHA-256
`ce4a199604e3120dfd2cf64647e60491ab507a10b2dfe3f3a1970bc2c95f9bc7`.
It uses a wider radix search in C and Mojo, recipe selection across valid
traces, and shorter programs from [Asterios catalog v61](notices/asterios-v61.md).

The previous verified candidate is `artifacts/santa-2026-136210.csv.enc`, score
`136210`, and SHA-256
`38d788f34b7832e88eb1250778b654875b9c61f64ca3a9e41f3ab2f7347be5d6`.
It combines shorter programs from the Apache-licensed
[DAG-LNS program bank](notices/dag-lns-v1.md) with native C recipe search.

The previous verified candidate is `artifacts/santa-2026-136189.csv.enc`, score
`136189`, and SHA-256
`cede8b6c50bc852a05a008e9396236e638deb1a08e8138816dc8bf0d9909cf28`.
It combines shorter programs from [Asterios catalog v63](notices/asterios-v63.md)
with three programs generated by a new run of the
[DAG-LNS reference solver](notices/dag-lns-v1.md).

The previous verified candidate is `artifacts/santa-2026-136178.csv.enc`, score
`136178`, and SHA-256
`1940748686995246ee95460fb22fc6a4eaa3b3d9644f3dd97eceff26217c0b14`.
It combines shorter programs from [Asterios catalog v64](notices/asterios-v64.md)
with C recipe search on programs including
[Alex Chilton’s Rudolph bank](https://www.kaggle.com/datasets/alexchilton/santa-2026-rudolph-programs)
and [Santiago Zazo’s verified bank](https://www.kaggle.com/datasets/santiagozazo/santa-2026-137792-verified-bank).

The previous verified candidate is `artifacts/santa-2026-136166.csv.enc`, score
`136166`, and SHA-256
`1406f9b87b1221b0925080db8da59acc02eca3abcfe7f7a2a27eb2073bd83a3e`.
It combines Mojo dependency-graph rewrites, C fan-out and wide-radix
rewrites, and shorter programs from [Asterios catalog v65](notices/asterios-v65.md).

The previous verified candidate is `artifacts/santa-2026-136149.csv.enc`, score
`136149`, and SHA-256
`7fc9128ad3ec45c78e06a5d6bc367154e9f8161f93317441becc71b97e67f89b`.
It combines shorter programs from [Asterios catalog v66](notices/asterios-v66.md)
and the [updated Rudolph bank](notices/rudolph-0030.md) with native C fan-out,
wide-radix, and recipe rewrites. The fan-out pass supplies equal-cost
derivations for downstream searches.

The previous verified candidate is `artifacts/santa-2026-136146.csv.enc`, score
`136146`, and SHA-256
`09599436287259142a3dd90897802efdef2f1dbd452a6feb308dbed81378cd82`.
It shortens `scored_0416` by three instructions using the
[updated Asterios snapshot](notices/asterios-0042.md) and two native C
recipe passes. The last pass lets two consumers switch to a shared
operand together.

The current candidate is `artifacts/santa-2026-136058.csv.enc`, score
`136058`, and SHA-256
`ea0708f3e82e341903124d2d9b249df1b5a7698e9563e1e2efc80cfb243cc6ef`.
It combines shorter programs from the [DAG-LNS snapshot](notices/dag-lns-0052.md)
and [Asterios snapshot](notices/asterios-0102.md) with a local DAG-LNS run.
The native C and Mojo solvers combine arithmetic recipes collected during
the local runs. Both solvers replay their chosen programs before release.
