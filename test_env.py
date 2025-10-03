#!/usr/bin/env python3
"""
Simple test script to verify environment variables are loaded correctly
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_env_vars():
    """Test if environment variables are loaded correctly"""
    print("Testing environment variables from .env file:")
    
    # Test each environment variable
    env_vars = {
        'ACCOUNT_NUMBER': os.getenv('ACCOUNT_NUMBER'),
        'CERT_FILE': os.getenv('CERT_FILE'),
        'CERT_PASS': os.getenv('CERT_PASS'),
        'XIBMCLIENTID': os.getenv('XIBMCLIENTID')
    }
    
    for var_name, var_value in env_vars.items():
        if var_value:
            print(f"✓ {var_name}: {'*' * len(var_value) if 'PASS' in var_name else var_value}")
        else:
            print(f"✗ {var_name}: Not found or empty")
    
    # Check if certificate file exists
    cert_file = env_vars['CERT_FILE']
    if cert_file and os.path.exists(cert_file):
        print(f"✓ Certificate file exists: {cert_file}")
    else:
        print(f"✗ Certificate file not found: {cert_file}")

if __name__ == "__main__":
    test_env_vars()