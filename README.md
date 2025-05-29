# RBCZ Premium API Library

This library provides a Python interface to the Raiffeisenbank CZ Premium API.

## Features
- Fetch account details
- Download statements
- Retrieve transaction lists

## Installation

Install the library using pip:

```bash
pip install rbczpremiumapi
```

## Usage

```python
from rbczpremiumapi import PremiumAPI

# Initialize the API client
client = PremiumAPI(client_id='your_client_id')

# Fetch account details
accounts = client.get_accounts()
print(accounts)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
