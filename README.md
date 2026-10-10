# entirius-py-edrone-sdk

A Python client for the edrone marketing automation REST API, part of Entirius, the open-source modular ecommerce platform.
It syncs a customer's newsletter subscription to edrone through one `EdroneClient` class.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-edrone-sdk.svg)](https://pypi.org/project/entirius-py-edrone-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-edrone-sdk.svg)](https://pypi.org/project/entirius-py-edrone-sdk/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-edrone-sdk/blob/develop/LICENSE)

## What it does

- Subscribes or unsubscribes a customer (`sub_or_unsub_customer_subscription()`).
- Carries the email, the tags and the subscription status in one typed `SubscribeEdrone` DTO.
- Adds the application id and the API version to every payload (`authorize()`).
- Raises `EdroneError` when the API answers with an error or an unexpected body.

## Installation

```shell
uv add entirius-py-edrone-sdk
pip install entirius-py-edrone-sdk
```

The import name is `edrone_sdk`.

## Quick start

```python
from edrone_sdk.dto.customer import SubscribeEdrone
from edrone_sdk.services.client import EdroneClient

edrone = EdroneClient(app_id="...")
ok, response = edrone.sub_or_unsub_customer_subscription(
    sub_data=SubscribeEdrone(email="user@example.com", customer_tags="", subscriber_status=0),
)
```

## Requirements

- Python 3.11 or newer.
- `requests` (installed as a dependency).
- An edrone account (application id).

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-edrone-sdk/blob/develop/CHANGELOG.md

## Part of Entirius

This SDK is one of the marketing integration clients used by the Entirius backend service (Volkanos).

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Sibling marketing SDKs: https://github.com/entirius/entirius-py-get-response-sdk, https://github.com/entirius/entirius-py-salesmanago-sdk, https://github.com/entirius/entirius-py-synerise-sdk

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest); the integration test is skipped without EDRONE_APP_ID
```

Development and agent instructions: https://github.com/entirius/entirius-py-edrone-sdk/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-edrone-sdk/blob/develop/LICENSE.
