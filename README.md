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
