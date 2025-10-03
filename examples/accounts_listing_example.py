#!/usr/bin/env python3
"""
Complete working example showing how to get account listing using the RBC Premium API library.
This demonstrates proper library usage patterns for the generated Python client.

IMPORTANT: This example shows the proper usage pattern. Due to template generation issues,
you may need to fix imports first by running:
1. Fix imports in rbczpremiumapi/__init__.py (change absolute to relative imports)
2. Run this example to test the library

Requirements:
- Valid RBC Premium API credentials (X-IBM-Client-Id)
- Client certificate in PKCS#12 format (.p12 file)
- Certificate password
"""
import os
import sys
import tempfile
import json
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

# Add the library path - adjust if needed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Load environment variables
load_dotenv()

# Environment configuration
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')
CERT_FILE = os.getenv('CERT_FILE')
CERT_PASS = os.getenv('CERT_PASS')


# Note: extract_p12_certificate is now available as ApiClient.extract_p12_certificate()
# This avoids code duplication and makes the function available to all library users


def get_accounts_with_library(use_sandbox: bool = False) -> Optional[List[Dict[str, Any]]]:
    """
    Get account listing using the RBC Premium API library.
    This is the proper way to use the generated client library.
    """
    print("🏦 RBC Premium API - Get Account Listing (Using Library)")
    print("="*70)
    
    # Step 1: Import the library components
    print("📚 Step 1: Importing library components...")
    
    try:
        # Import the main library components
        # NOTE: You may need to fix import paths first in rbczpremiumapi/__init__.py
        from rbczpremiumapi import Configuration, ApiClient
        from rbczpremiumapi import GetAccountsApi
        from rbczpremiumapi.exceptions import ApiException
        print("✅ Library components imported successfully")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Please fix import paths in rbczpremiumapi/__init__.py first")
        print("   Change absolute imports (from PremiumAPI.xxx) to relative (from .PremiumAPI.xxx)")
        return None
    
    # Step 2: Validate environment
    print("🔧 Step 2: Validating environment...")
    if not all([X_IBM_CLIENT_ID, CERT_FILE, CERT_PASS]):
        print("❌ Missing required environment variables:")
        print("   - XIBMCLIENTID: API client ID")
        print("   - CERT_FILE: Path to .p12 certificate file")
        print("   - CERT_PASS: Certificate password")
        return None
    
    if not os.path.exists(CERT_FILE):
        print(f"❌ Certificate file not found: {CERT_FILE}")
        return None
    
    print("✅ Environment validation passed")
    
    # Step 3: Extract certificates for mTLS
    print("🔐 Step 3: Extracting certificates for mTLS authentication...")
    cert_path, key_path = ApiClient.extract_p12_certificate(CERT_FILE, CERT_PASS)
    if not cert_path or not key_path:
        print("❌ Failed to extract certificate and key from .p12 file")
        return None
    print("✅ Certificates extracted successfully")
    
    try:
        # Step 4: Configure the API client
        print("⚙️  Step 4: Configuring API client...")
        
        # Create configuration object
        config = Configuration()
        
        # Set the API host
        if use_sandbox:
            config.host = "https://api.rb.cz/rbcz/premium/mock"
            print("🧪 Using SANDBOX environment")
        else:
            config.host = "https://api.rb.cz/rbcz/premium/api"
            print("🏭 Using PRODUCTION environment")
        
        # Configure API key authentication
        config.api_key = {'X-IBM-Client-Id': X_IBM_CLIENT_ID}
        
        # Configure mTLS certificate authentication
        config.cert_file = cert_path
        config.key_file = key_path
        config.verify_ssl = True
        
        # Optional: Configure timeouts and retries
        # config.timeout = 30
        # config.retries = 3
        
        print(f"✅ API client configured for: {config.host}")
        
        # Step 5: Create API client and accounts API instance
        print("🔌 Step 5: Creating API client and service instances...")
        
        # Create the main API client
        api_client = ApiClient(config)
        
        # Create the GetAccountsApi instance
        accounts_api = GetAccountsApi(api_client)
        
        print("✅ API instances created successfully")
        
        # Step 6: Make the API call
        print("📡 Step 6: Calling API to get account listing...")
        
        try:
            # Call the get_accounts method
            # This returns a typed response object with validation
            response = accounts_api.get_accounts()
            
            print("✅ API call successful!")
            
            # Step 7: Process the typed response
            print("📊 Step 7: Processing response...")
            
            # Convert response to dictionary for easier handling
            if hasattr(response, 'to_dict'):
                accounts_data = response.to_dict()
            elif hasattr(response, 'dict'):
                accounts_data = response.dict()
            else:
                accounts_data = response
            
            # Extract accounts array from response
            accounts = accounts_data.get('accounts', [])
            return accounts
            
        except ApiException as api_ex:
            print(f"❌ API Exception occurred:")
            print(f"   Status Code: {api_ex.status}")
            print(f"   Reason: {api_ex.reason}")
            if hasattr(api_ex, 'body') and api_ex.body:
                try:
                    error_body = json.loads(api_ex.body)
                    print(f"   Error Details: {json.dumps(error_body, indent=2)}")
                except:
                    print(f"   Raw Error Body: {api_ex.body}")
            return None
        
        except Exception as e:
            print(f"❌ Unexpected error during API call: {e}")
            return None
        
    finally:
        # Step 8: Cleanup temporary certificate files
        print("🧹 Step 8: Cleaning up temporary files...")
        try:
            if cert_path:
                os.unlink(cert_path)
            if key_path:
                os.unlink(key_path)
        except:
            pass
        print("✅ Cleanup completed")


def print_accounts_details(accounts: List[Dict[str, Any]]):
    """
    Print formatted account listing information from the API response.
    """
    print("\n" + "="*70)
    print(f"🏦 ACCOUNT LISTING REPORT")
    print("="*70)
    
    if not accounts:
        print("❌ No accounts found")
        return
    
    print(f"📊 Total Accounts Found: {len(accounts)}")
    print()
    
    for idx, account in enumerate(accounts, 1):
        # Extract account information with safe defaults
        account_id = account.get('account_id', 'Unknown')
        account_name = account.get('account_name', 'Unknown')
        iban = account.get('iban', 'Unknown')
        currency = account.get('currency', 'Unknown')
        balance = account.get('balance', None)
        
        print(f"💳 Account {idx}: {account_name}")
        print(f"   🆔 Account ID: {account_id}")
        print(f"   🏧 IBAN: {iban}")
        print(f"   💱 Currency: {currency}")
        
        # Format balance if available
        if balance is not None:
            try:
                formatted_balance = f"{float(balance):,.2f}"
                print(f"   💰 Balance: {formatted_balance} {currency}")
            except (ValueError, TypeError):
                print(f"   💰 Balance: {balance}")
        else:
            print(f"   💰 Balance: Not available")
        
        # Display additional account details if available
        additional_fields = [
            ('account_type', 'Account Type', '📋'),
            ('status', 'Status', '📊'),
            ('product_name', 'Product', '📦'),
            ('owner_name', 'Owner', '👤'),
            ('branch_code', 'Branch', '🏢')
        ]
        
        for field_key, field_label, icon in additional_fields:
            if field_key in account and account[field_key]:
                print(f"   {icon} {field_label}: {account[field_key]}")
        
        print()  # Empty line between accounts
    
    print("="*70)


def demonstrate_account_operations():
    """
    Demonstrate other account-related operations available in the library.
    """
    print("\n🔧 OTHER AVAILABLE ACCOUNT OPERATIONS")
    print("="*50)
    
    print("The library provides additional account operations:")
    print()
    
    print("1. 💰 Get Account Balance:")
    print("   balance_api = GetAccountBalanceApi(api_client)")
    print("   response = balance_api.get_balance(account_number)")
    print()
    
    print("2. 📋 Get Transaction List:")
    print("   transaction_api = GetTransactionListApi(api_client)")
    print("   response = transaction_api.get_transaction_list(account_number, from_date, to_date)")
    print()
    
    print("3. 📄 Get Statement List:")
    print("   statement_api = GetStatementListApi(api_client)")
    print("   response = statement_api.get_statement_list(account_number)")
    print()
    
    print("4. 📥 Download Statement:")
    print("   download_api = DownloadStatementApi(api_client)")
    print("   response = download_api.download_statement(statement_request)")
    print()
    
    print("5. 💸 Upload Payments:")
    print("   payments_api = UploadPaymentsApi(api_client)")
    print("   response = payments_api.upload_payments(payment_data)")
    print()
    
    print("6. 💱 Get FX Rates:")
    print("   fx_api = GetFxRatesApi(api_client)")
    print("   response = fx_api.get_fx_rates(currency_pair)")
    print()


def main():
    """
    Main function demonstrating complete library usage for account listing.
    """
    print("🏦 RBC Premium API Python Library - Account Listing Example")
    print("📋 Demonstration: Complete Account Information Retrieval")
    print("="*70)
    
    # Environment status check
    print("🔧 Environment Configuration:")
    print(f"   X-IBM-Client-ID: {'✅ Set' if X_IBM_CLIENT_ID else '❌ Missing'}")
    print(f"   Certificate File: {'✅ Found' if CERT_FILE and os.path.exists(CERT_FILE) else '❌ Missing'}")
    print(f"   Certificate Password: {'✅ Set' if CERT_PASS else '❌ Missing'}")
    print()
    
    # Attempt to use the library
    accounts = get_accounts_with_library(use_sandbox=False)
    
    if accounts:
        # Success - print the account information
        print_accounts_details(accounts)
        
        print("\n🎉 SUCCESS!")
        print("✅ Library usage demonstrated successfully")
        print("✅ Type-safe API calls with proper authentication")
        print("✅ Structured response handling and validation")
        print("✅ Complete account information retrieved")
        
    else:
        print("\n📝 DEMONSTRATION NOTES")
        print("💡 This example shows the proper library usage pattern")
        print("🔧 Fix any import issues in the generated library first")
        print("🔑 Ensure valid API credentials are configured")
    
    # Show additional operations
    demonstrate_account_operations()
    
    print("\n🚀 NEXT STEPS:")
    print("   1. Fix import paths in rbczpremiumapi/__init__.py if needed")
    print("   2. Configure valid API credentials in .env file")
    print("   3. Run this example to test the library")
    print("   4. Explore other API operations (balance, transactions, etc.)")
    print("   5. Build your application using the type-safe library!")
    
    print("\n📚 LIBRARY ADVANTAGES:")
    print("   ✅ Type safety with Pydantic models")
    print("   ✅ Automatic request/response validation")
    print("   ✅ IDE autocompletion and error detection")
    print("   ✅ Structured exception handling")
    print("   ✅ Built-in authentication handling")
    print("   ✅ Professional error messages")


if __name__ == "__main__":
    main()