#!/usr/bin/env python3
"""
Integration test for the RBCZ Premium API library
"""
import os
from dotenv import load_dotenv
import rbczpremiumapi

# Load environment variables from .env file
load_dotenv()

def test_api_client_creation():
    """Test creating an API client with environment variables"""
    print("Testing API client creation...")
    
    try:
        # Get environment variables
        client_id = os.getenv('XIBMCLIENTID')
        cert_file = os.getenv('CERT_FILE')
        cert_pass = os.getenv('CERT_PASS')
        
        if not all([client_id, cert_file, cert_pass]):
            print("✗ Missing required environment variables")
            return False
            
        print(f"✓ Client ID: {client_id[:8]}...")
        print(f"✓ Certificate file: {cert_file}")
        
        # Try to create a client instance
        client = rbczpremiumapi.PremiumAPI(
            client_id=client_id,
            cert_file=cert_file,
            cert_password=cert_pass
        )
        
        print("✓ API client created successfully")
        return True
        
    except Exception as e:
        print(f"✗ Error creating API client: {e}")
        return False

if __name__ == "__main__":
    success = test_api_client_creation()
    exit(0 if success else 1)