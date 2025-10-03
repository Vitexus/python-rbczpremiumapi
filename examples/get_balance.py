#!/usr/bin/env python3
"""
Complete example that gets and prints account balance using the RBC Premium API.
This example demonstrates both direct HTTP requests and library usage.
"""
import os
import sys
import requests
import tempfile
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Add the library path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import ApiClient for certificate extraction
try:
    from rbczpremiumapi.api_client import ApiClient
except ImportError:
    # Fallback for development or when library isn't properly installed
    print("Warning: Could not import ApiClient, using fallback certificate extraction")
    ApiClient = None

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
    
    This function now uses ApiClient.extract_p12_certificate() if available,
    otherwise falls back to a basic implementation.
    """
    if ApiClient is not None:
        # Use the shared implementation from ApiClient
        return ApiClient.extract_p12_certificate(cert_file, cert_pass)
    else:
        # Fallback implementation - requires manual cryptography import
        print("Warning: Using fallback certificate extraction")
        print("For better integration, ensure rbczpremiumapi library is properly installed")
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.primitives.serialization import pkcs12
            
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


def get_account_balance_direct(account_number: str, use_sandbox: bool = False) -> Optional[Dict[str, Any]]:
    """
    Get account balance using direct HTTP requests.
    
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
    
    # Extract certificate and key from PKCS#12 file
    print("🔐 Extracting certificate and key from PKCS#12 file...")
    cert_path, key_path = extract_p12_certificate(CERT_FILE, CERT_PASS)
    if not cert_path or not key_path:
        print("❌ Failed to extract certificate and key")
        return None
    
    try:
        # Choose API endpoint based on environment
        if use_sandbox:
            base_url = "https://api.rb.cz/rbcz/premium/mock"
            print("🧪 Using SANDBOX endpoints")
        else:
            base_url = "https://api.rb.cz/rbcz/premium/api"
            print("🏭 Using PRODUCTION endpoints")
        
        # API endpoint for getting account balance
        balance_url = f"{base_url}/accounts/{account_number}/balance"
        
        headers = {
            "X-IBM-Client-Id": X_IBM_CLIENT_ID,
            "X-Request-Id": "get-balance-123",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        print(f"🌐 Making request to: {balance_url}")
        print(f"📋 Headers: {headers}")
        
        # Make request with client certificate authentication
        response = requests.get(
            balance_url,
            headers=headers,
            cert=(cert_path, key_path),
            verify=True,
            timeout=30
        )
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            balance_data = response.json()
            print("✅ Account balance retrieved successfully!")
            return balance_data
        else:
            print(f"❌ Failed to get account balance: {response.status_code}")
            print(f"📄 Response: {response.text}")
            return None
            
    except requests.exceptions.SSLError as e:
        print(f"🔒 SSL Error: {e}")
        print("💡 This might be due to certificate issues or API access restrictions")
        return None
    except requests.exceptions.RequestException as e:
        print(f"🌐 Request error: {e}")
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
    
    # Print raw data structure first
    print(f"📄 Raw API Response:")
    print(json.dumps(balance_data, indent=2, ensure_ascii=False))
    
    # Try to parse and display structured balance information
    print(f"\n💵 BALANCE DETAILS:")
    
    # The balance response structure according to OpenAPI spec should have currencyFolders
    currency_folders = balance_data.get('currencyFolders', [])
    
    if currency_folders:
        for folder in currency_folders:
            currency = folder.get('currency', 'Unknown')
            print(f"\n💱 Currency: {currency}")
            
            balances = folder.get('balances', [])
            for balance in balances:
                balance_type = balance.get('balanceType', balance.get('type', 'Unknown'))
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
        
        # Try alternative structure
        if 'amount' in balance_data:
            amount = balance_data['amount']
            currency = balance_data.get('currency', 'CZK')
            print(f"💸 Balance: {amount:,.2f} {currency}")
    
    print("="*60)


def try_library_approach():
    """
    Demonstrate how to use the generated library classes (when imports are fixed).
    This shows the intended usage pattern.
    """
    print("\n🔧 LIBRARY APPROACH (Conceptual - requires import fixes)")
    print("="*60)
    
    try:
        # This is how it SHOULD work once the import issues are resolved
        print("📚 Step 1: Import library components")
        print("   from rbczpremiumapi import Configuration, ApiClient")
        print("   from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi")
        print("   from rbczpremiumapi.Model.get_balance200_response import GetBalance200Response")
        
        print("\n⚙️  Step 2: Configure API client")
        print("   config = Configuration()")
        print("   config.host = 'https://api.rb.cz'")
        print("   config.api_key['X-IBM-Client-Id'] = 'your-client-id'")
        print("   # Note: Certificate configuration would need additional setup")
        
        print("\n🔌 Step 3: Create API instance and make call")
        print("   api_client = ApiClient(config)")
        print("   balance_api = GetAccountBalanceApi(api_client)")
        print("   response = balance_api.get_balance(account_number='123456')")
        
        print("\n📊 Step 4: Process response")
        print("   balance_data = response.to_dict()")
        print("   # Use structured model objects for type safety")
        
        # Try actual import test
        try:
            from rbczpremiumapi.configuration import Configuration
            print("✅ Configuration import works")
            
            from rbczpremiumapi.api_client import ApiClient  
            print("✅ ApiClient import works")
            
            # This will likely fail due to import issues
            from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi
            print("✅ GetAccountBalanceApi import works")
            
        except ImportError as e:
            print(f"❌ Import failed: {e}")
            print("💡 This is expected due to the import issues in generated files")
            print("🔧 Solution: Fix the template imports and regenerate")
            
    except Exception as e:
        print(f"❌ Library approach failed: {e}")
    
    print("="*60)


def main():
    """
    Main function to demonstrate getting account balance.
    """
    print("🏦 RBC Premium API - Account Balance Example")
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
    
    # Method 1: Direct HTTP requests (production)
    print("\n" + "="*60)
    print("🌐 METHOD 1: Direct HTTP Requests (Production API)")
    print("="*60)
    
    balance_data = get_account_balance_direct(account_number, use_sandbox=False)
    if balance_data:
        print_balance_info(balance_data, account_number)
    else:
        print("❌ Failed to get balance from production API")
    
    # Method 2: Try sandbox if production fails
    print("\n" + "="*60)  
    print("🧪 METHOD 2: Direct HTTP Requests (Sandbox API)")
    print("="*60)
    
    balance_data_sandbox = get_account_balance_direct(account_number, use_sandbox=True)
    if balance_data_sandbox:
        print_balance_info(balance_data_sandbox, account_number)
    else:
        print("❌ Failed to get balance from sandbox API")
    
    # Method 3: Show library approach
    try_library_approach()
    
    # Final summary
    print("\n" + "="*60)
    print("📋 SUMMARY")
    print("="*60)
    
    if balance_data or balance_data_sandbox:
        print("✅ Successfully demonstrated API connectivity and balance retrieval")
        print("✅ Certificate extraction and mTLS authentication working")
        print("✅ API request formatting and response handling working")
    else:
        print("⚠️  API requests failed - this may be due to:")
        print("   • Network connectivity issues")
        print("   • Invalid or expired certificates")
        print("   • API access restrictions")
        print("   • Incorrect account numbers")
    
    print("🔧 Next steps:")
    print("   • Fix library import issues in templates")
    print("   • Test with valid API credentials")
    print("   • Implement proper error handling")
    print("   • Add support for multiple accounts")


if __name__ == "__main__":
    main()
