# casvisor-python-sdk

[![GitHub Actions](https://github.com/casvisor/casvisor-python-sdk/workflows/build/badge.svg)](https://github.com/casvisor/casvisor-python-sdk/actions)
[![Version](https://img.shields.io/pypi/v/casvisor-python-sdk.svg)](https://pypi.org/project/casvisor-python-sdk/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/casvisor-python-sdk.svg)](https://pypi.org/project/casvisor-python-sdk/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casvisor-python-sdk.svg)](https://pypi.org/project/casvisor-python-sdk/)
[![Discord](https://img.shields.io/discord/1022748306096537660?logo=discord&label=discord&color=5865F2)](https://discord.gg/5rPsrAzK7S)

Casvisor Python SDK is the official Python client for [Casvisor](https://github.com/casvisor/casvisor), used to interact with Casvisor services.

Casvisor-python-sdk is available on PyPI:

```console
pip install casvisor-python-sdk
```

Casvisor SDK is simple to use. We will show you the steps below.


## Init Config

Initialization requires 5 parameters, which are all str type:

| Name (in order)  | Must | Description                                           |
| ---------------- | ---- | ----------------------------------------------------- |
| endpoint         | Yes  | Casvisor Server Url, such as `http://localhost:16001` |
| clientId         | Yes  | Application.clientId                                  |
| clientSecret     | Yes  | Application.clientSecret                              |
| organizationName | Yes  | Organization name                                     |
| applicationName  | Yes  | Application name                                      |

```python
from casvisor-python-sdk import CasvisorSDK

sdk = CasvisorSDK(
    endpoint,
    clientId,
    clientSecret,
    organizationName,
    applicationName,
)
```


## Basic Usage

casvisor-python-sdk supports some basic operations, such as:

- `get_records(self)`, get all records
- `get_record(self, name: str)`, get one record by name
- `get_pagination_records(self, p: int, pageSize: int, query_map: Dict[str, str])`, get records by pagination
- `update_record(self, record: Record)`, update one record
- `add_record(self, record: Record)`, add one record
- `delete_record(self, record: Record)`, delete one record


## Test

Run test:

```console
pip install -r requirements.txt
python -m unittest discover src/tests -v
```


## Contribution

We welcome any form of contribution, including but not limited to:

1. Submit issues and suggestions
2. Submit Pull Request
3. Improve documentation


## License

This project is licensed under the [Apache 2.0 License](LICENSE).