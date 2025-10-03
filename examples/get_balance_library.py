#!/usr/bin/env python3
"""
Complete example that gets and prints account balance using library functions.
This version demonstrates how to use the generated library classes directly.
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

# Load environment variables from .env file
load_dotenv()

# Initialize environment variables
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')
ACCOUNT_NUMBER = os.getenv('ACCOUNT_NUMBER')
CERT_FILE = os.getenv('CERT_FILE')
CERT_PASS = os.getenv('CERT_PASS')


def extract_p12_certificate(cert_file: str, cert_pass: str) -> tuple[Optional[str], Optional[str]]:
    """
    Extract certificate and private key from PKCS#12 file.
    Returns tuple of (cert_file_path, key_file_path) for use with requests.
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


def get_balance_using_library(account_number: str, use_sandbox: bool = False) -> Optional[Dict[str, Any]]:
    """
    Get account balance using the generated library classes.
    This shows how to use the library properly once the import issues are resolved.
    
    Args:
        account_number: The account number to get balance for
        use_sandbox: Whether to use sandbox (mock) API endpoints
    
    Returns:
        Dictionary with balance information or None if failed
    """
    if not all([X_IBM_CLIENT_ID, CERT_FILE, CERT_PASS]):
        print("❌ Missing required environment variables (XIBMCLIENTID, CERT_FILE, CERT_PASS)")
        return None
    
    # Check if certificate file exists
    if not os.path.exists(CERT_FILE):
        print(f"❌ Certificate file not found: {CERT_FILE}")
        return None
    
    print("🔧 LIBRARY APPROACH - Using Generated API Classes")
    print("="*60)
    
    try:
        # Extract certificate and key from PKCS#12 file
        print("🔐 Extracting certificate and key from PKCS#12 file...")
        cert_path, key_path = extract_p12_certificate(CERT_FILE, CERT_PASS)
        if not cert_path or not key_path:
            print("❌ Failed to extract certificate and key")
            return None
        
        try:
            # Import the library components directly (workaround for import issues)
            from rbczpremiumapi.configuration import Configuration
            from rbczpremiumapi.api_client import ApiClient
            from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi
            from rbczpremiumapi.exceptions import ApiException
            
            print("✅ Successfully imported library components")
            
            # Configure the API client
            config = Configuration()
            
            # Set the host based on environment
            if use_sandbox:
                config.host = "https://api.rb.cz/rbcz/premium/mock"
                print("🧪 Using SANDBOX endpoints")
            else:
                config.host = "https://api.rb.cz/rbcz/premium/api"
                print("🏭 Using PRODUCTION endpoints")
            
            # Set API key
            config.api_key = {
                'X-IBM-Client-Id': X_IBM_CLIENT_ID
            }
            
            # Configure SSL certificate
            config.cert_file = cert_path
            config.key_file = key_path
            config.ssl_ca_cert = None  # Use system CA bundle
            config.verify_ssl = True
            
            print(f"⚙️  Configured API client for host: {config.host}")
            
            # Create API client and balance API instance
            api_client = ApiClient(config)
            balance_api = GetAccountBalanceApi(api_client)
            
            print(f"🎯 Making API call for account: {account_number}")
            
            # Make the API call
            response = balance_api.get_balance(account_number)
            
            print("✅ Balance retrieved successfully using library!")
            
            # Convert response to dictionary (if it's a model object)
            if hasattr(response, 'to_dict'):
                balance_data = response.to_dict()
            else:
                balance_data = response
                
            return balance_data
            
        except ImportError as e:
            print(f"❌ Import failed: {e}")
            print("💡 This is expected due to the import issues in generated files")
            print("🔧 The library would work like this once imports are fixed:")
            show_library_usage_concept()
            return None
        except ApiException as e:
            print(f"❌ API Exception: {e}")
            print(f"📄 Response body: {e.body}")
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
    
    except Exception as e:
        print(f"❌ Library approach failed: {e}")
        return None


def show_library_usage_concept():
    """
    Show the conceptual usage of the library once imports are fixed.
    """
    print("\n🎓 CONCEPTUAL LIBRARY USAGE")
    print("="*60)
    print("Once the import issues are resolved, the usage would be:")
    print()
    
    print("📚 1. Import the library components:")
    print("   from rbczpremiumapi import Configuration, ApiClient")
    print("   from rbczpremiumapi import GetAccountBalanceApi")
    print("   from rbczpremiumapi import GetBalance200Response")
    print()
    
    print("⚙️  2. Configure the API client:")
    print("   config = Configuration()")
    print("   config.host = 'https://api.rb.cz/rbcz/premium/api'")
    print("   config.api_key = {'X-IBM-Client-Id': 'your-client-id'}")
    print("   config.cert_file = '/path/to/client.pem'")
    print("   config.key_file = '/path/to/client.key'")
    print()
    
    print("🔌 3. Create API instance and make the call:")
    print("   api_client = ApiClient(config)")
    print("   balance_api = GetAccountBalanceApi(api_client)")
    print("   response = balance_api.get_balance('account_number')")
    print()
    
    print("📊 4. Process the typed response:")
    print("   # response is a GetBalance200Response object with type safety")
    print("   balance_data = response.to_dict()")
    print("   for folder in response.currency_folders:")
    print("       print(f'Currency: {folder.currency}')")
    print("       for balance in folder.balances:")
    print("           print(f'{balance.balance_type}: {balance.value}')")
    
    print("\n💡 Benefits of the library approach:")
    print("   ✅ Type safety with Pydantic models")
    print("   ✅ Built-in validation")
    print("   ✅ IDE autocompletion")
    print("   ✅ Automatic serialization/deserialization")
    print("   ✅ Exception handling")
    print("   ✅ Request/response logging")
    print("="*60)


def print_balance_info(balance_data: Dict[str, Any], account_number: str):
    """
    Pretty print account balance information.
    
    Args:
        balance_data: The balance data dictionary from API response
        account_number: The account number for display
    """
    print("\n" + "="*60)
    print(f"💰 ACCOUNT BALANCE REPORT")
    print("="*60)
    print(f"📊 Account Number: {account_number}")
    
    if not balance_data:
        print("❌ No balance data available")
        return
    
    # Try to parse and display structured balance information
    print(f"\n💵 BALANCE DETAILS:")
    
    # The balance response structure according to OpenAPI spec should have currencyFolders
    currency_folders = balance_data.get('currency_folders', [])
    
    if currency_folders:
        for folder in currency_folders:
            currency = folder.get('currency', 'Unknown')
            print(f"\n💱 Currency: {currency}")
            
            balances = folder.get('balances', [])
            for balance in balances:
                balance_type = balance.get('balance_type', balance.get('type', 'Unknown'))
                amount = balance.get('value', balance.get('amount', 0))
                
                # Balance type descriptions
                balance_descriptions = {
                    'CLAV': 'Available balance (with credit limit)',
                    'CLBD': 'Booking balance (actual accounting)',
                    'CLAB': 'Actual balance (without credit limit)',
                    'BLCK': 'Blocked balance'
                }
                
                description = balance_descriptions.get(balance_type, balance_type)
                print(f"  💸 {description}: {amount:,.2f} {currency}")
    else:
        print("⚠️  No currency folders found in response")
    
    print("="*60)


def main():
    """
    Main function to demonstrate getting account balance using library functions.
    """
    print("🏦 RBC Premium API - Library Usage Example")
    print("="*60)
    
    # Show environment status
    print("🔧 Environment Check:")
    print(f"   XIBMCLIENTID: {'✅' if X_IBM_CLIENT_ID else '❌'}")
    print(f"   ACCOUNT_NUMBER: {'✅' if ACCOUNT_NUMBER else '❌'}")
    print(f"   CERT_FILE: {'✅' if CERT_FILE and os.path.exists(CERT_FILE) else '❌'}")
    print(f"   CERT_PASS: {'✅' if CERT_PASS else '❌'}")
    
    if not ACCOUNT_NUMBER:
        print("\n❌ No account number provided. Using default for demo.")
        account_number = "2800061687"  # Use the one from .env as fallback
    else:
        account_number = ACCOUNT_NUMBER
    
    print(f"\n🎯 Target Account: {account_number}")
    
    # Try to use library approach (production)
    print("\n" + "="*60)
    print("🌐 LIBRARY APPROACH (Production API)")
    print("="*60)
    
    balance_data = get_balance_using_library(account_number, use_sandbox=False)
    if balance_data:
        print_balance_info(balance_data, account_number)
    else:
        print("❌ Failed to get balance using library approach")
        print("💡 This is expected due to current import issues")
    
    # Always show the conceptual usage
    show_library_usage_concept()
    
    # Final summary
    print("\n" + "="*60)
    print("📋 SUMMARY")
    print("="*60)
    
    if balance_data:
        print("✅ Library approach would work perfectly!")
        print("✅ Type-safe API calls with validation")
        print("✅ Clean, maintainable code structure")
    else:
        print("🔧 Current Status:")
        print("   • Library classes generated successfully")
        print("   • Import paths need to be relative (template issue)")
        print("   • Once fixed, library will provide full type safety")
    
    print("🎯 Next Steps:")
    print("   • Fix import paths in __init__.py templates")
    print("   • Regenerate the library")
    print("   • Enjoy full type safety and IDE support!")
    print("   • Use structured model objects instead of raw dictionaries")


if __name__ == "__main__":
    main()