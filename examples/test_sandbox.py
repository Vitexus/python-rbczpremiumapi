#!/usr/bin/env python3
"""
Sandbox example for testing the RBC Premium API using mock endpoints.
This version uses the sandbox endpoints for testing without real transactions.
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

def test_sandbox_endpoints():
    """
    Test sandbox endpoints using the mock API.
    According to the sandbox specification, test certificate is available with password 'Test12345678'.
    """
    if not X_IBM_CLIENT_ID:
        print("Missing XIBMCLIENTID environment variable.")
        return
    
    # Sandbox base URL (mock endpoints)
    base_url = "https://api.rb.cz/rbcz/premium/mock"
    
    headers = {
        "X-IBM-Client-Id": X_IBM_CLIENT_ID,
        "X-Request-Id": "sandbox-test-123",
        "Accept-Language": "en",
        "Content-Type": "application/json"
    }
    
    # Test 1: Get FX Rates (no certificate required)
    print("=== Test 1: Get FX Rates (No Certificate Required) ===")
    fx_url = f"{base_url}/fxrates"
    
    try:
        response = requests.get(fx_url, headers=headers, timeout=10)
        print(f"FX Rates Response: {response.status_code}")
        if response.status_code == 200:
            fx_data = response.json()
            print(f"FX Rates data keys: {list(fx_data.keys()) if fx_data else 'No data'}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"FX Rates error: {e}")
    
    print()
    
    # Test 2: Get specific currency FX rate (no certificate required)
    print("=== Test 2: Get EUR FX Rates (No Certificate Required) ===")
    eur_fx_url = f"{base_url}/fxrates/EUR"
    
    try:
        response = requests.get(eur_fx_url, headers=headers, timeout=10)
        print(f"EUR FX Response: {response.status_code}")
        if response.status_code == 200:
            print(f"EUR FX data: {response.json()}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"EUR FX error: {e}")
    
    print()
    
    # Test 3: Try certificate-required endpoint (will fail without proper cert)
    print("=== Test 3: Get Accounts (Certificate Required - Expected to Fail) ===")
    accounts_url = f"{base_url}/accounts"
    
    try:
        response = requests.get(accounts_url, headers=headers, timeout=10)
        print(f"Accounts Response: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Accounts error (expected): {e}")
    
    print()
    
    # Test 4: Show what a proper certificate test would look like
    print("=== Test 4: Certificate Test (Mock) ===")
    print("For real certificate testing, you would:")
    print("1. Download test certificate from: https://api.rb.cz/assets/test_cert.p12")
    print("2. Use password: Test12345678")
    print("3. Extract certificate using cryptography library")
    print("4. Make requests with client certificate authentication")
    
    if CERT_FILE and os.path.exists(CERT_FILE):
        print(f"Local certificate file found: {CERT_FILE}")
        print("This could be used for authenticated requests.")
    else:
        print("No local certificate file configured.")


if __name__ == "__main__":
    print("=== RBC Premium API Sandbox Testing ===")
    print()
    
    # Show environment status
    print("Environment variables:")
    print(f"  XIBMCLIENTID: {'✓' if X_IBM_CLIENT_ID else '✗'}")
    print(f"  ACCOUNT_NUMBER: {'✓' if ACCOUNT_NUMBER else '✗'}")
    print(f"  CERT_FILE: {'✓' if CERT_FILE else '✗'}")
    print(f"  CERT_PASS: {'✓' if CERT_PASS else '✗'}")
    print()
    
    print("🧪 Testing sandbox endpoints...")
    print("Note: Sandbox uses '/rbcz/premium/mock/' endpoints")
    print("      Production uses '/rbcz/premium/api/' endpoints")
    print()
    
    test_sandbox_endpoints()