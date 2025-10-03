#!/usr/bin/env python3
"""
Direct example of downloading statements using the rbczpremiumapi library.
This bypasses the generated API classes which have syntax errors.
"""
import os
import sys
import requests
import tempfile
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

def extract_p12_certificate(cert_file, cert_pass):
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


def download_statements_direct():
    """
    Download statements using direct HTTP requests with proper authentication.
    """
    if not all([X_IBM_CLIENT_ID, ACCOUNT_NUMBER, CERT_FILE, CERT_PASS]):
        print("Missing required environment variables. Please check your .env file.")
        print(f"XIBMCLIENTID: {'✓' if X_IBM_CLIENT_ID else '✗'}")
        print(f"ACCOUNT_NUMBER: {'✓' if ACCOUNT_NUMBER else '✗'}")
        print(f"CERT_FILE: {'✓' if CERT_FILE else '✗'}")
        print(f"CERT_PASS: {'✓' if CERT_PASS else '✗'}")
        return
    
    # Check if certificate file exists
    if not os.path.exists(CERT_FILE):
        print(f"Certificate file not found: {CERT_FILE}")
        return
    
    # Extract certificate and key from PKCS#12 file
    print("Extracting certificate and key from PKCS#12 file...")
    cert_path, key_path = extract_p12_certificate(CERT_FILE, CERT_PASS)
    if not cert_path or not key_path:
        print("Failed to extract certificate and key.")
        return
    
    # Base URL for Raiffeisenbank Premium API (Production)
    # For sandbox testing, use: "https://api.rb.cz/rbcz/premium/mock"
    # For production, use: "https://api.rb.cz/rbcz/premium/api"
    base_url = "https://api.rb.cz/rbcz/premium/api"
    
    # First, let's get the list of statements
    statements_url = f"{base_url}/accounts/statements"
    
    headers = {
        "X-IBM-Client-Id": X_IBM_CLIENT_ID,
        "X-Request-Id": "test-request-123",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    
    # Request body for getting statements list
    request_data = {
        "accountNumber": ACCOUNT_NUMBER,
        "dateFrom": "2024-01-01",
        "dateTo": "2024-12-31"
    }
    
    try:
        print("Attempting to get statements list...")
        print(f"URL: {statements_url}")
        print(f"Headers: {headers}")
        print(f"Request data: {request_data}")
        
        # Make request with client certificate
        response = requests.post(
            statements_url,
            json=request_data,
            headers=headers,
            cert=(cert_path, key_path),
            verify=True,  # Verify SSL certificates
            timeout=30
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            statements = response.json()
            print("Statements retrieved successfully:")
            print(statements)
            
            # If we have statements, try to download the first one
            if statements and 'statements' in statements and len(statements['statements']) > 0:
                first_statement = statements['statements'][0]
                statement_id = first_statement.get('statementId')
                
                if statement_id:
                    download_statement(statement_id, headers, cert_path, key_path)
            else:
                print("No statements found in the response.")
        else:
            print(f"Failed to get statements list: {response.status_code}")
            print(f"Response text: {response.text}")
            
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        print("This might be due to certificate issues. Please check your .p12 file and password.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Clean up temporary certificate files
        try:
            if cert_path:
                os.unlink(cert_path)
            if key_path:
                os.unlink(key_path)
        except:
            pass


def download_statement(statement_id, headers, cert_path, key_path):
    """
    Download a specific statement by ID.
    """
    base_url = "https://api.rb.cz/rbcz/premium/api"
    download_url = f"{base_url}/accounts/statements/download"
    
    download_data = {
        "statementId": statement_id,
        "format": "PDF"  # or XML, MT940, etc.
    }
    
    try:
        print(f"Attempting to download statement {statement_id}...")
        
        response = requests.post(
            download_url,
            json=download_data,
            headers=headers,
            cert=(cert_path, key_path),
            verify=True,
            timeout=30
        )
        
        if response.status_code == 200:
            filename = f"statement_{statement_id}.pdf"
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Statement downloaded successfully as {filename}")
        else:
            print(f"Failed to download statement: {response.status_code}")
            print(f"Response text: {response.text}")
            
    except Exception as e:
        print(f"Error downloading statement: {e}")


if __name__ == "__main__":
    print("=== RBC Premium API Statement Download Test ===")
    print()
    
    # Show environment status
    print("Environment variables:")
    print(f"  XIBMCLIENTID: {'✓' if X_IBM_CLIENT_ID else '✗'}")
    print(f"  ACCOUNT_NUMBER: {'✓' if ACCOUNT_NUMBER else '✗'}")
    print(f"  CERT_FILE: {'✓' if CERT_FILE else '✗'}")
    print(f"  CERT_PASS: {'✓' if CERT_PASS else '✗'}")
    print()
    
    download_statements_direct()