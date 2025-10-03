#!/usr/bin/env python3
"""
Complete example that gets and prints account listing using the RBC Premium API.
This example demonstrates both direct HTTP requests and library usage.
"""
import os
import sys
import requests
import tempfile
import json
from typing import Optional, List, Dict, Any
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


def get_accounts_direct(use_sandbox: bool = False) -> Optional[List[Dict[str, Any]]]:
    """
    Get accounts listing using direct HTTP requests.
    
    Args:
        use_sandbox: Whether to use sandbox (mock) API endpoints
    
    Returns:
        List of account dictionaries or None if failed
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
        
        # API endpoint for getting accounts
        accounts_url = f"{base_url}/accounts"
        
        headers = {
            "X-IBM-Client-Id": X_IBM_CLIENT_ID,
            "X-Request-Id": "get-accounts-123",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        print(f"🌐 Making request to: {accounts_url}")
        print(f"📋 Headers: {headers}")
        
        # Make request with client certificate authentication
        response = requests.get(
            accounts_url,
            headers=headers,
            cert=(cert_path, key_path),
            verify=True,
            timeout=30
        )
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            accounts_data = response.json()
            print("✅ Accounts listing retrieved successfully!")
            return accounts_data.get('accounts', [])
        else:
            print(f"❌ Failed to get accounts: {response.status_code}")
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


def get_accounts_using_library(use_sandbox: bool = False) -> Optional[List[Dict[str, Any]]]:
    """
    Get accounts listing using the generated library classes.
    This shows how to use the library properly once the import issues are resolved.
    
    Args:
        use_sandbox: Whether to use sandbox (mock) API endpoints
    
    Returns:
        List of account dictionaries or None if failed
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
            from rbczpremiumapi.PremiumAPI.get_accounts_api import GetAccountsApi
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
            
            # Create API client and accounts API instance
            api_client = ApiClient(config)
            accounts_api = GetAccountsApi(api_client)
            
            print(f"🎯 Making API call for accounts listing")
            
            # Make the API call
            response = accounts_api.get_accounts()
            
            print("✅ Accounts listing retrieved successfully using library!")
            
            # Convert response to dictionary (if it's a model object)
            if hasattr(response, 'to_dict'):
                accounts_data = response.to_dict()
                return accounts_data.get('accounts', [])
            else:
                return response.get('accounts', []) if isinstance(response, dict) else []
                
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
    print("   from rbczpremiumapi import GetAccountsApi")
    print("   from rbczpremiumapi import GetAccounts200Response")
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
    print("   accounts_api = GetAccountsApi(api_client)")
    print("   response = accounts_api.get_accounts()")
    print()
    
    print("📊 4. Process the typed response:")
    print("   # response is a GetAccounts200Response object with type safety")
    print("   accounts_data = response.to_dict()")
    print("   for account in response.accounts:")
    print("       print(f'Account: {account.number_part2}')")
    print("       print(f'Currency: {account.currency}')")
    print("       print(f'Product: {account.product_i18n_code}')")
    
    print("\n💡 Benefits of the library approach:")
    print("   ✅ Type safety with Pydantic models")
    print("   ✅ Built-in validation")
    print("   ✅ IDE autocompletion")
    print("   ✅ Automatic serialization/deserialization")
    print("   ✅ Exception handling")
    print("   ✅ Request/response logging")
    print("="*60)


def print_accounts_info(accounts: List[Dict[str, Any]]):
    """
    Pretty print accounts information.
    
    Args:
        accounts: List of account dictionaries from API response
    """
    print("\n" + "="*80)
    print(f"🏦 ACCOUNTS LISTING")
    print("="*80)
    
    if not accounts:
        print("❌ No accounts available")
        return
    
    print(f"📊 Total Accounts Found: {len(accounts)}")
    print()
    
    for i, account in enumerate(accounts, 1):
        print(f"🏛️  ACCOUNT #{i}")
        print("-" * 60)
        
        # Account identification
        account_number = account.get('accountNumber', 'Unknown')
        account_prefix = account.get('accountNumberPrefix', '')
        bank_code = account.get('bankCode', 'Unknown')
        
        if account_prefix:
            full_number = f"{account_prefix}-{account_number}/{bank_code}"
        else:
            full_number = f"{account_number}/{bank_code}"
        
        print(f"   📋 Account Number: {full_number}")
        
        # Account identification and names
        account_id = account.get('accountId', 'Unknown')
        account_name = account.get('accountName', 'Unknown')
        friendly_name = account.get('friendlyName', '')
        
        print(f"   🆔 Account ID: {account_id}")
        print(f"   � Account Name: {account_name}")
        if friendly_name:
            print(f"   🏷️  Friendly Name: {friendly_name}")
        
        # Basic account information
        main_currency = account.get('mainCurrency') or 'Not specified'
        print(f"   💱 Main Currency: {main_currency}")
        
        # Account type
        account_type_id = account.get('accountTypeId', 'Unknown')
        print(f"   🔖 Account Type: {account_type_id}")
        
        # Additional information if available
        if 'iban' in account:
            print(f"   � IBAN: {account['iban']}")
        
        if 'bankBicCode' in account and account['bankBicCode']:
            print(f"   🏦 BIC: {account['bankBicCode']}")
        
        # Show raw data for debugging (commented out by default)
        # print(f"   📄 Raw Data: {json.dumps(account, indent=2, ensure_ascii=False)}")
        
        print()
    
    print("="*80)


def main():
    """
    Main function to demonstrate getting accounts listing.
    """
    print("🏦 RBC Premium API - Accounts Listing Example")
    print("="*80)
    
    # Show environment status
    print("🔧 Environment Check:")
    print(f"   XIBMCLIENTID: {'✅' if X_IBM_CLIENT_ID else '❌'}")
    print(f"   CERT_FILE: {'✅' if CERT_FILE and os.path.exists(CERT_FILE) else '❌'}")
    print(f"   CERT_PASS: {'✅' if CERT_PASS else '❌'}")
    
    # Method 1: Direct HTTP requests (production)
    print("\n" + "="*80)
    print("🌐 METHOD 1: Direct HTTP Requests (Production API)")
    print("="*80)
    
    accounts_data = get_accounts_direct(use_sandbox=False)
    if accounts_data:
        print_accounts_info(accounts_data)
    else:
        print("❌ Failed to get accounts from production API")
    
    # Method 2: Try sandbox if production fails or for comparison
    print("\n" + "="*80)  
    print("🧪 METHOD 2: Direct HTTP Requests (Sandbox API)")
    print("="*80)
    
    accounts_data_sandbox = get_accounts_direct(use_sandbox=True)
    if accounts_data_sandbox:
        print_accounts_info(accounts_data_sandbox)
    else:
        print("❌ Failed to get accounts from sandbox API")
    
    # Method 3: Library approach (will show conceptual usage)
    print("\n" + "="*80)
    print("🔧 METHOD 3: Library Functions Approach")
    print("="*80)
    
    library_accounts = get_accounts_using_library(use_sandbox=False)
    if library_accounts:
        print("✅ Library approach worked!")
        print_accounts_info(library_accounts)
    else:
        print("❌ Library approach failed (expected due to import issues)")
    
    # Final summary
    print("\n" + "="*80)
    print("📋 SUMMARY")
    print("="*80)
    
    if accounts_data or accounts_data_sandbox or library_accounts:
        print("✅ Successfully demonstrated API connectivity and accounts retrieval")
        print("✅ Certificate extraction and mTLS authentication working")
        print("✅ API request formatting and response handling working")
        
        # Show account count summary
        prod_count = len(accounts_data) if accounts_data else 0
        sandbox_count = len(accounts_data_sandbox) if accounts_data_sandbox else 0
        lib_count = len(library_accounts) if library_accounts else 0
        
        print(f"📊 Accounts found:")
        print(f"   • Production API: {prod_count} accounts")
        print(f"   • Sandbox API: {sandbox_count} accounts") 
        print(f"   • Library API: {lib_count} accounts")
    else:
        print("⚠️  API requests failed - this may be due to:")
        print("   • Network connectivity issues")
        print("   • Invalid or expired certificates")
        print("   • API access restrictions")
        print("   • Account access permissions")
    
    print("🔧 Next steps:")
    print("   • Fix library import issues in templates")
    print("   • Test with valid API credentials")
    print("   • Implement proper error handling")
    print("   • Add support for account filtering and pagination")


if __name__ == "__main__":
    main()
