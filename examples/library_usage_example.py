#!/usr/bin/env python3
"""
Complete working example showing how to get account balance using the RBC Premium API library.
This demonstrates proper library usage patterns for the generated Python client.

IMPORTANT: This example shows the proper usage pattern. Due to template generation issues,
you may need to fix imports first by running:
1. Fix imports in rbczpremiumapi/__init__.py (change absolute to relative imports)
2. Run this example to test the library

Requirements:
- Valid RBC Premium API credentials (X-IBM-Client-Id)
- Client certificate in PKCS#12 format (.p12 file)
- Certificate password
- Account number to query
"""
import os
import sys
import tempfile
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Add the library path - adjust if needed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Load environment variables
load_dotenv()

# Environment configuration
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')
ACCOUNT_NUMBER = os.getenv('ACCOUNT_NUMBER', '2800061687')
CERT_FILE = os.getenv('CERT_FILE')
CERT_PASS = os.getenv('CERT_PASS')


# Note: extract_p12_certificate is now available as ApiClient.extract_p12_certificate()
# This avoids code duplication and makes the function available to all library users


def get_account_balance_with_library(account_number: str, use_sandbox: bool = False) -> Optional[Dict[str, Any]]:
    """
    Get account balance using the RBC Premium API library.
    This is the proper way to use the generated client library.
    """
    print("🏦 RBC Premium API - Get Account Balance (Using Library)")
    print("="*70)
    
    # Step 1: Import the library components
    print("📚 Step 1: Importing library components...")
    
    try:
        # Import the main library components
        from rbczpremiumapi.configuration import Configuration
        from rbczpremiumapi.api_client import ApiClient
        from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi
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
        
        # Step 5: Create API client and balance API instance
        print("🔌 Step 5: Creating API client and service instances...")
        
        # Create the main API client
        api_client = ApiClient(config)
        
        # Create the GetAccountBalanceApi instance
        balance_api = GetAccountBalanceApi(api_client)
        
        print("✅ API instances created successfully")
        
        # Step 6: Make the API call
        print(f"📡 Step 6: Calling API to get balance for account: {account_number}")
        
        try:
            # Call the get_balance method
            # This returns a typed response object with validation
            import uuid
            x_request_id = str(uuid.uuid4())  # Generate unique request ID
            response = balance_api.get_balance(
                x_ibm_client_id=X_IBM_CLIENT_ID,
                x_request_id=x_request_id, 
                account_number=account_number
            )
            
            print("✅ API call successful!")
            
            # Step 7: Process the typed response
            print("📊 Step 7: Processing response...")
            
            # Convert response to dictionary for easier handling
            if hasattr(response, 'to_dict'):
                balance_data = response.to_dict()
            elif hasattr(response, 'dict'):
                balance_data = response.dict()
            else:
                balance_data = response
            
            return balance_data
            
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


def print_balance_details(balance_data: Dict[str, Any], account_number: str):
    """
    Print formatted balance information from the API response.
    """
    print("\n" + "="*70)
    print(f"💰 ACCOUNT BALANCE REPORT")
    print("="*70)
    print(f"📊 Account Number: {account_number}")
    
    if not balance_data:
        print("❌ No balance data available")
        return
    
    # Process currency folders from the response
    currency_folders = balance_data.get('currency_folders', [])
    
    if not currency_folders:
        print("⚠️  No currency folders found in response")
        print(f"📝 Raw response structure: {list(balance_data.keys())}")
        return
    
    print(f"\n💵 Balance Information:")
    
    for folder_idx, folder in enumerate(currency_folders, 1):
        currency = folder.get('currency', 'Unknown')
        status = folder.get('status', 'Unknown')
        
        print(f"\n💱 Currency Folder {folder_idx}: {currency}")
        print(f"   📊 Status: {status}")
        
        # Process balances within the currency folder
        balances = folder.get('balances', [])
        
        if not balances:
            print("   ⚠️  No balances found in this currency folder")
            continue
        
        for balance_idx, balance in enumerate(balances, 1):
            balance_type = balance.get('balance_type', 'Unknown')
            amount = balance.get('value', 0)
            
            # Balance type descriptions for better understanding
            balance_descriptions = {
                'CLAV': 'Available Balance (including credit limit)',
                'CLBD': 'Booking Balance (actual accounting balance)', 
                'CLAB': 'Actual Balance (without credit limit)',
                'BLCK': 'Blocked Balance'
            }
            
            description = balance_descriptions.get(balance_type, balance_type)
            
            # Format amount with proper currency symbol
            try:
                formatted_amount = f"{float(amount):,.2f}"
            except (ValueError, TypeError):
                formatted_amount = str(amount)
            
            print(f"   💸 Balance {balance_idx}: {description}")
            print(f"      💰 Amount: {formatted_amount} {currency}")
            print(f"      🏷️  Type Code: {balance_type}")
    
    print("="*70)


def demonstrate_error_handling():
    """
    Demonstrate proper error handling with the library.
    """
    print("\n🛡️ ERROR HANDLING DEMONSTRATION")
    print("="*50)
    
    print("The library provides structured error handling:")
    print()
    
    print("1. 📡 API Exceptions (ApiException):")
    print("   - HTTP status codes (401, 403, 404, 429, etc.)")
    print("   - Structured error messages from the API")
    print("   - Rate limiting information")
    print()
    
    print("2. 🔍 Validation Exceptions:")
    print("   - Input parameter validation")
    print("   - Response format validation")
    print("   - Type safety enforcement")
    print()
    
    print("3. 🌐 Network Exceptions:")
    print("   - Connection timeouts")
    print("   - SSL/TLS certificate errors")
    print("   - DNS resolution failures")
    print()
    
    print("Example error handling pattern:")
    print("""
    try:
        response = balance_api.get_balance(account_number)
        return response.to_dict()
    except ApiException as api_ex:
        if api_ex.status == 401:
            print("Authentication failed - check credentials")
        elif api_ex.status == 403:
            print("Access forbidden - check permissions")
        elif api_ex.status == 429:
            print("Rate limit exceeded - wait before retrying")
        else:
            print(f"API error: {api_ex.status} - {api_ex.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    """)


def main():
    """
    Main function demonstrating complete library usage.
    """
    print("🏦 RBC Premium API Python Library - Complete Example")
    print("📋 Demonstration: Account Balance Retrieval")
    print("="*70)
    
    # Environment status check
    print("🔧 Environment Configuration:")
    print(f"   X-IBM-Client-ID: {'✅ Set' if X_IBM_CLIENT_ID else '❌ Missing'}")
    print(f"   Certificate File: {'✅ Found' if CERT_FILE and os.path.exists(CERT_FILE) else '❌ Missing'}")
    print(f"   Certificate Password: {'✅ Set' if CERT_PASS else '❌ Missing'}")
    print(f"   Account Number: {ACCOUNT_NUMBER}")
    print()
    
    # Attempt to use the library
    balance_data = get_account_balance_with_library(ACCOUNT_NUMBER, use_sandbox=False)
    
    if balance_data:
        # Success - print the balance information
        print_balance_details(balance_data, ACCOUNT_NUMBER)
        
        print("\n🎉 SUCCESS!")
        print("✅ Library usage demonstrated successfully")
        print("✅ Type-safe API calls with proper authentication")
        print("✅ Structured response handling and validation")
        print("✅ Professional error handling")
        
    else:
        print("\n📝 DEMONSTRATION NOTES")
        print("💡 This example shows the proper library usage pattern")
        print("🔧 Fix any import issues in the generated library first")
        print("🔑 Ensure valid API credentials are configured")
    
    # Show error handling information
    demonstrate_error_handling()
    
    print("\n🚀 NEXT STEPS:")
    print("   1. Fix import paths in rbczpremiumapi/__init__.py if needed")
    print("   2. Configure valid API credentials in .env file")
    print("   3. Run this example to test the library")
    print("   4. Use similar patterns for other API operations")
    print("   5. Enjoy type-safe, validated API interactions!")


if __name__ == "__main__":
    main()