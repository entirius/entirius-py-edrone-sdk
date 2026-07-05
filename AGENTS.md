# AGENTS.md

edrone marketing automation SDK — distribution `entirius-py-edrone-sdk`, import `edrone_sdk`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `edrone_sdk` — it is a public API contract.
- Default: do not commit — git is the user's call.

## Architecture

- `services/client.py` — `EdroneClient`: builds an authorized payload and posts subscription changes to `/trace`.
- `services/request.py` — thin HTTP wrapper over `requests`.
- `dto/` — `AuthDTO`, `SubscribeEdrone` (request), `SubscribeResponse` (response).
- `validators/` — response shape validation.
- Integration test hits the live edrone API — skipped unless `EDRONE_APP_ID` is set.
