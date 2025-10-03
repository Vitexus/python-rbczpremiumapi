# RBC Premium API Python Library - Examples

This folder contains working examples demonstrating how to use the RBC Premium API Python library. These examples show the proper usage patterns for the generated client library.

## 📁 Example Files

### 🏦 Core Library Usage Examples

1. **`library_usage_example.py`** - Complete account balance retrieval example
   - Demonstrates proper library import and configuration
   - Shows mTLS certificate handling
   - Includes comprehensive error handling
   - Shows response processing and formatting

2. **`accounts_listing_example.py`** - Account listing retrieval example
   - Shows how to get all accounts for a client
   - Demonstrates account information processing
   - Includes formatting and display of account details

### 🔧 Direct API Examples (For Reference)

3. **`get_balance.py`** - Direct HTTP API call for balance (reference implementation)
4. **`get_accounts.py`** - Direct HTTP API call for accounts (reference implementation)

## 🚀 Quick Start

### Prerequisites

1. **API Credentials**: Valid RBC Premium API credentials
2. **Certificate**: Client certificate in PKCS#12 format (.p12 file)
3. **Environment**: Python virtual environment with required dependencies

### Setup Environment Variables

Create a `.env` file in the project root:

```bash
# RBC Premium API Configuration
XIBMCLIENTID=your-client-id-here
CERT_FILE=/path/to/your/certificate.p12
CERT_PASS=your-certificate-password
ACCOUNT_NUMBER=your-account-number
```

### Run Examples

#### Library Usage Examples (Recommended)

```bash
# Account balance example using library
python examples/library_usage_example.py

# Account listing example using library  
python examples/accounts_listing_example.py
```

#### Direct API Examples (Reference Only)

```bash
# Direct API calls (for reference)
python examples/get_balance.py
python examples/get_accounts.py
```

## 📚 Library Usage Patterns

### Basic Library Import and Setup

```python
from rbczpremiumapi import Configuration, ApiClient
from rbczpremiumapi import GetAccountBalanceApi, GetAccountsApi
from rbczpremiumapi.exceptions import ApiException

# Configure API client
config = Configuration()
config.host = "https://api.rb.cz/rbcz/premium/api"  # Production
# config.host = "https://api.rb.cz/rbcz/premium/mock"  # Sandbox

# Authentication
config.api_key = {'X-IBM-Client-Id': 'your-client-id'}
config.cert_file = '/path/to/cert.pem'
config.key_file = '/path/to/key.pem'

# Create API client
api_client = ApiClient(config)
```

### Making API Calls

```python
# Get account balance
balance_api = GetAccountBalanceApi(api_client)
try:
    response = balance_api.get_balance('your-account-number')
    balance_data = response.to_dict()
except ApiException as e:
    print(f"API Error: {e.status} - {e.reason}")

# Get account listing
accounts_api = GetAccountsApi(api_client)
try:
    response = accounts_api.get_accounts()
    accounts = response.to_dict()['accounts']
except ApiException as e:
    print(f"API Error: {e.status} - {e.reason}")
```

## 🔧 Troubleshooting

### Import Issues

If you encounter import errors, you may need to fix import paths in the generated library:

1. **Check**: `rbczpremiumapi/__init__.py`
2. **Fix**: Change absolute imports to relative imports:
   ```python
   # Wrong (absolute)
   from PremiumAPI.get_accounts_api import GetAccountsApi
   
   # Correct (relative)
   from .PremiumAPI.get_accounts_api import GetAccountsApi
   ```

### Common Issues

1. **Certificate Issues**: Ensure your .p12 certificate file exists and password is correct
2. **Network Issues**: Check firewall and proxy settings for API connectivity
3. **Authentication Issues**: Verify X-IBM-Client-Id is valid and active
4. **Import Issues**: Fix relative imports in the generated library files

## 🎯 Available API Operations

The library provides these main API operations:

- **`GetAccountsApi`** - List all accounts
- **`GetAccountBalanceApi`** - Get account balance details
- **`GetTransactionListApi`** - Get transaction history
- **`GetStatementListApi`** - List available statements
- **`DownloadStatementApi`** - Download statement files
- **`UploadPaymentsApi`** - Upload payment instructions
- **`GetFxRatesApi`** - Get foreign exchange rates
- **`GetFxRatesListApi`** - Get FX rates for multiple currencies

## 💡 Best Practices

1. **Use Library Functions**: Always use the generated library instead of direct HTTP calls
2. **Error Handling**: Implement proper exception handling with `ApiException`
3. **Certificate Security**: Keep certificate files secure and use environment variables
4. **Rate Limiting**: Respect API rate limits (10/second, 5000/day)
5. **Type Safety**: Leverage Pydantic models for type safety and validation

## 📖 Further Reading

- **API Documentation**: See `docs/` folder for detailed API documentation
- **OpenAPI Specification**: `01rbczpremiumapi.yaml` contains the complete API specification
- **Library Architecture**: See project README.md for library structure details

## 🆘 Support

For issues with:
- **API Access**: Contact RBC Premium API support
- **Library Issues**: Check GitHub issues or create new issue
- **Certificate Issues**: Contact your RBC Premium banking representative

---

**Note**: The examples in this folder demonstrate the **intended** library usage. Make sure to fix any import path issues in the generated library before running the examples.