# edrone-sdk

edrone marketing automation SDK — customer subscription sync over the edrone REST API.

## Installation

```shell
pip install entirius-py-edrone-sdk
```

## Usage

```python
from edrone_sdk.services.client import EdroneClient
from edrone_sdk.dto.customer import SubscribeEdrone

edrone = EdroneClient(app_id="...")
response, ok = edrone.sub_or_unsub_customer_subscription(
    sub_data=SubscribeEdrone(email="user@example.com", subscriber_status=0),
)
```

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest) — integration test skipped without EDRONE_APP_ID
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
