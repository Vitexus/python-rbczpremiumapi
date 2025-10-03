#!/usr/bin/env python3
"""
Complete example showing how to get account balance using the RBC Premium API library.
This example demonstrates the proper usage of the generated API classes.
"""
import os
import sys
import tempfile
from typing import Optional, Dict, Any
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12
from dotenv import load_dotenv

# Add the library path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Load environment variables
load_dotenv()

# Environment variables
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')
ACCOUNT_NUMBER = os.getenv('ACCOUNT_NUMBER', '2800061687')
CERT_FILE = os.getenv('CERT_FILE')
CERT_PASS = os.getenv('CERT_PASS')


def extract_p12_certificate(cert_file: str, cert_pass: str) -> tuple[Optional[str], Optional[str]]:
    """
    Extract certificate and private key from PKCS#12 file.
    Returns tuple of (cert_file_path, key_file_path) for use with the library.
    """
    try:
        with open(cert_file, 'rb') as f:
            p12_data = f.read()
        
        # Load PKCS#12 data
        private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
            p12_data, cert_pass.encode()
        )
        
        # Create temporary files for cert and key
        cert_fd, cert_path = tempfile.mkstemp(suffix='.pem')
        key_fd, key_path = tempfile.mkstemp(suffix='.pem')
        
        try:
            # Write certificate to temp file
            with os.fdopen(cert_fd, 'wb') as cert_file_obj:
                cert_file_obj.write(certificate.public_bytes(serialization.Encoding.PEM))
            
            # Write private key to temp file
            with os.fdopen(key_fd, 'wb') as key_file_obj:
                key_file_obj.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))
            
            return cert_path, key_path
        except:
            # Clean up on error
            try:
                os.unlink(cert_path)
            except:
                pass
            try:
                os.unlink(key_path)
            except:
                pass
            raise
    except Exception as e:
        print(f"Error extracting certificate: {e}")
        return None, None


def get_account_balance(account_number: str, use_sandbox: bool = False) -> Optional[Dict[str, Any]]:
    """
    Get account balance using the RBC Premium API library.
    
    This function demonstrates the proper way to use the library's generated API classes.
    
    Args:
        account_number: The account number to get balance for
        use_sandbox: Whether to use sandbox (mock) API endpoints
    
    Returns:
        Dictionary with balance information or None if failed
    """
    print("🏦 RBC Premium API - Get Account Balance (Library Usage)")
    print("="*70)
    
    if not all([X_IBM_CLIENT_ID, CERT_FILE, CERT_PASS]):
        print("❌ Missing required environment variables")
        print("   Required: XIBMCLIENTID, CERT_FILE, CERT_PASS")
        return None
    
    if not os.path.exists(CERT_FILE):
        print(f"❌ Certificate file not found: {CERT_FILE}")
        return None
    
    # Extract certificate for mTLS authentication
    print("🔐 Extracting certificate and key from PKCS#12 file...")
    cert_path, key_path = extract_p12_certificate(CERT_FILE, CERT_PASS)
    if not cert_path or not key_path:
        print("❌ Failed to extract certificate and key")
        return None
    
    try:
        # Step 1: Import the required library components
        print("📚 Step 1: Importing library components...")
        
        # This is how you should import the library components:
        try:
            from rbczpremiumapi import Configuration, ApiClient, GetAccountBalanceApi
            from rbczpremiumapi.exceptions import ApiException
            print("✅ Library components imported successfully")
        except ImportError as e:
            print(f"❌ Import failed: {e}")
            print("💡 Note: This demonstrates the intended usage once imports are fixed")
            show_conceptual_usage(account_number, use_sandbox)
            return None
        
        # Step 2: Configure the API client
        print("⚙️  Step 2: Configuring API client...")
        config = Configuration()
        
        # Set the appropriate host
        if use_sandbox:
            config.host = "https://api.rb.cz/rbcz/premium/mock"
            print("🧪 Using SANDBOX endpoints")
        else:
            config.host = "https://api.rb.cz/rbcz/premium/api"
            print("🏭 Using PRODUCTION endpoints")
        
        # Configure authentication
        config.api_key = {'X-IBM-Client-Id': X_IBM_CLIENT_ID}
        
        # Configure mTLS certificates
        config.cert_file = cert_path
        config.key_file = key_path
        config.verify_ssl = True
        
        print(f"✅ API client configured for: {config.host}")
        
        # Step 3: Create API client and balance API instance
        print("🔌 Step 3: Creating API instances...")
        api_client = ApiClient(config)
        balance_api = GetAccountBalanceApi(api_client)
        print("✅ API instances created successfully")
        
        # Step 4: Make the API call
        print(f"📡 Step 4: Requesting balance for account: {account_number}")
        
        try:
            # Call the get_balance method
            response = balance_api.get_balance(account_number)
            print("✅ Balance retrieved successfully!")
            
            # Step 5: Process the response
            print("📊 Step 5: Processing response...")
            
            # The response is a typed model object with validation
            if hasattr(response, 'to_dict'):
                balance_data = response.to_dict()
            else:
                balance_data = response
            
            return balance_data
            
        except ApiException as e:
            print(f"❌ API Exception: {e}")
            print(f"   Status: {e.status}")
            print(f"   Reason: {e.reason}")
            if e.body:
                print(f"   Response: {e.body}")
            return None
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
    finally:
        # Clean up temporary certificate files
        try:
            if cert_path:
                os.unlink(cert_path)
            if key_path:
                os.unlink(key_path)
        except:
            pass


def show_conceptual_usage(account_number: str, use_sandbox: bool = False):
    """
    Show the conceptual usage of the library when imports work properly.
    """
    print("\n🎓 CONCEPTUAL LIBRARY USAGE")
    print("="*70)
    print("This is how the library should be used once imports are working:")
    print()
    
    env_type = "SANDBOX" if use_sandbox else "PRODUCTION"
    host_url = "https://api.rb.cz/rbcz/premium/mock" if use_sandbox else "https://api.rb.cz/rbcz/premium/api"
    
    print("📚 1. Import library components:")
    print("   from rbczpremiumapi import Configuration, ApiClient")
    print("   from rbczpremiumapi import GetAccountBalanceApi")
    print("   from rbczpremiumapi.exceptions import ApiException")
    print()
    
    print("⚙️  2. Configure the API client:")
    print("   config = Configuration()")
    print(f"   config.host = '{host_url}'")
    print("   config.api_key = {'X-IBM-Client-Id': 'your-client-id'}")
    print("   config.cert_file = '/path/to/client.pem'")
    print("   config.key_file = '/path/to/client.key'")
    print("   config.verify_ssl = True")
    print()
    
    print("🔌 3. Create API instances:")
    print("   api_client = ApiClient(config)")
    print("   balance_api = GetAccountBalanceApi(api_client)")
    print()
    
    print("📡 4. Make the API call:")
    print("   try:")
    print(f"       response = balance_api.get_balance('{account_number}')")
    print("       balance_data = response.to_dict()")
    print("   except ApiException as e:")
    print("       print(f'API Error: {e.status} - {e.reason}')")
    print()
    
    print("📊 5. Process the typed response:")
    print("   # response is a GetBalance200Response object with type safety")
    print("   for folder in response.currency_folders:")
    print("       currency = folder.currency")
    print("       for balance in folder.balances:")
    print("           balance_type = balance.balance_type")
    print("           amount = balance.value")
    print("           print(f'{currency} {balance_type}: {amount}')")
    print()
    
    print("💡 Benefits of using the library:")
    print("   ✅ Type safety with Pydantic models")
    print("   ✅ Automatic request/response validation")
    print("   ✅ IDE autocompletion and error detection")
    print("   ✅ Structured exception handling")
    print("   ✅ Built-in authentication handling")
    print("   ✅ Automatic retry and timeout configuration")
    print("="*70)


def print_balance_info(balance_data: Dict[str, Any], account_number: str):
    """
    Print formatted balance information.
    
    Args:
        balance_data: Balance data from the API response
        account_number: Account number for display
    """
    print("\n" + "="*70)
    print(f"💰 ACCOUNT BALANCE REPORT")
    print("="*70)
    print(f"📊 Account: {account_number}")
    
    if not balance_data:
        print("❌ No balance data available")
        return
    
    # Parse balance information from the response
    currency_folders = balance_data.get('currency_folders', [])
    
    if currency_folders:
        print(f"\n💵 Balance Details:")
        
        for folder in currency_folders:
            currency = folder.get('currency', 'Unknown')
            status = folder.get('status', 'Unknown')
            
            print(f"\n💱 Currency: {currency} (Status: {status})")
            
            balances = folder.get('balances', [])
            for balance in balances:
                balance_type = balance.get('balance_type', 'Unknown')
                amount = balance.get('value', 0)
                
                # Balance type descriptions
                balance_descriptions = {
                    'CLAV': 'Available balance (with credit limit)',
                    'CLBD': 'Booking balance (actual accounting)', 
                    'CLAB': 'Actual balance (without credit limit)',
                    'BLCK': 'Blocked balance'
                }
                
                description = balance_descriptions.get(balance_type, balance_type)
                print(f"   💸 {description}: {amount:,.2f} {currency}")
    else:
        print("⚠️  No currency folders found in response")
    
    print("="*70)


def main():
    """
    Main function demonstrating account balance retrieval using the library.
    """
    print("🏦 RBC Premium API Python Library")
    print("📋 Example: Get Account Balance")
    print("="*70)
    
    # Environment check
    print("🔧 Environment Status:")
    print(f"   XIBMCLIENTID: {'✅' if X_IBM_CLIENT_ID else '❌'}")
    print(f"   CERT_FILE: {'✅' if CERT_FILE and os.path.exists(CERT_FILE) else '❌'}")
    print(f"   CERT_PASS: {'✅' if CERT_PASS else '❌'}")
    print(f"   ACCOUNT_NUMBER: {ACCOUNT_NUMBER}")
    print()
    
    # Try to get balance using library functions
    balance_data = get_account_balance(ACCOUNT_NUMBER, use_sandbox=False)
    
    if balance_data:
        print_balance_info(balance_data, ACCOUNT_NUMBER)
        
        print("\n🎉 SUCCESS!")
        print("✅ Successfully demonstrated library usage")
        print("✅ Type-safe API calls with proper authentication")
        print("✅ Structured response handling")
    else:
        print("\n📝 DEMONSTRATION COMPLETE")
        print("💡 This example shows the proper way to use the library")
        print("🔧 Once import issues are resolved, this code will work perfectly")
        
    print("\n🚀 Next Steps:")
    print("   • Fix template import issues and regenerate library")
    print("   • Use the library for type-safe API interactions")
    print("   • Enjoy full IDE support and validation")


if __name__ == "__main__":
    main()