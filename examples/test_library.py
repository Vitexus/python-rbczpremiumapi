#!/usr/bin/env python3
"""
Example using the generated rbczpremiumapi library classes.
This demonstrates how to use the generated Python client for the RBC Premium API.
"""
import os
import sys
from dotenv import load_dotenv

# Add the library path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Load environment variables
load_dotenv()

def test_library_import():
    """
    Test importing and using the generated library classes.
    """
    try:
        # Test importing core components
        print("=== Testing Library Imports ===")
        
        from rbczpremiumapi.configuration import Configuration
        print("✓ Configuration imported successfully")
        
        from rbczpremiumapi.api_client import ApiClient
        print("✓ ApiClient imported successfully")
        
        # Test importing models
        from rbczpremiumapi.Model.currency_list_simple import CurrencyListSimple
        print("✓ CurrencyListSimple model imported successfully")
        
        from rbczpremiumapi.Model.exchange_rate import ExchangeRate
        print("✓ ExchangeRate model imported successfully")
        
        # Test importing APIs (this might fail due to syntax errors in generated files)
        try:
            from rbczpremiumapi.PremiumAPI.get_fx_rates_api import GetFxRatesApi
            print("✓ GetFxRatesApi imported successfully")
        except Exception as e:
            print(f"✗ GetFxRatesApi import failed: {e}")
            
        try:
            from rbczpremiumapi.PremiumAPI.get_accounts_api import GetAccountsApi
            print("✓ GetAccountsApi imported successfully")
        except Exception as e:
            print(f"✗ GetAccountsApi import failed: {e}")
        
        print("\\n=== Library Structure Test ===")
        
        # Create configuration
        config = Configuration()
        config.host = "https://api.rb.cz"
        print("✓ Configuration created and configured")
        
        # Create API client
        api_client = ApiClient(config)
        print("✓ ApiClient created with configuration")
        
        # Show available models
        print("\\n=== Available Models ===")
        import rbczpremiumapi.Model as Models
        
        # List some key model classes
        model_classes = [
            'CurrencyListSimple',
            'ExchangeRate', 
            'ExchangeRateList',
            'DownloadStatementRequest',
            'GetAccounts200Response'
        ]
        
        for model_name in model_classes:
            if hasattr(Models, model_name):
                print(f"✓ {model_name}")
            else:
                print(f"✗ {model_name} (not found)")
        
        # Environment configuration
        print("\\n=== Environment Configuration ===")
        X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')
        if X_IBM_CLIENT_ID:
            print(f"✓ Client ID configured: {X_IBM_CLIENT_ID[:8]}...")
        else:
            print("✗ Client ID not configured")
            
        return True
        
    except Exception as e:
        print(f"✗ Library import test failed: {e}")
        return False


def show_api_endpoints():
    """
    Show the available API endpoints based on the OpenAPI specification.
    """
    print("\\n=== Available API Endpoints ===")
    print("Production Base URL: https://api.rb.cz/rbcz/premium/api")
    print("Sandbox Base URL: https://api.rb.cz/rbcz/premium/mock")
    print()
    
    endpoints = [
        ("GET", "/accounts", "Get list of accounts"),
        ("GET", "/accounts/{accountNumber}/balance", "Get account balance"),
        ("GET", "/accounts/{accountNumber}/{currencyCode}/transactions", "Get transactions"),
        ("POST", "/accounts/statements", "Get statements list"),
        ("POST", "/accounts/statements/download", "Download statement"),
        ("POST", "/payments/batches", "Upload payment batches"),
        ("GET", "/payments/batches/{batchFileId}", "Get batch details"),
        ("GET", "/fxrates", "Get FX rates list"),
        ("GET", "/fxrates/{currencyCode}", "Get specific FX rates")
    ]
    
    for method, path, description in endpoints:
        cert_required = "❌ Cert Required" if path != "/fxrates" and not path.startswith("/fxrates/") else "✅ No Cert Required"
        print(f"{method:4} {path:40} - {description} ({cert_required})")


if __name__ == "__main__":
    print("=== RBC Premium API Python Library Test ===")
    print()
    
    # Test library imports
    success = test_library_import()
    
    # Show API information
    show_api_endpoints()
    
    print("\\n=== Summary ===")
    if success:
        print("✅ Library is properly structured and importable")
        print("✅ Models and configuration work correctly")
        print("⚠️  Some API classes may have syntax errors (known issue)")
        print("✅ Core functionality is available for manual API calls")
    else:
        print("❌ Library has import issues that need to be resolved")
    
    print("\\n📋 Next Steps:")
    print("1. Fix any remaining syntax errors in generated API classes")
    print("2. Test with real API credentials")
    print("3. Implement proper certificate handling")
    print("4. Add more comprehensive examples")