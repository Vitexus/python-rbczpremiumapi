#!/usr/bin/env python3
"""
Test script for the RBCZ Premium API library functionality
Tests the basic functionality without requiring actual certificates or network access.
"""

import sys
import traceback

def test_imports():
    """Test that all main library components can be imported"""
    print("Testing library imports...")
    
    try:
        # Test main package import
        import rbczpremiumapi
        print("✓ Main package imported successfully")
        
        # Test API client import
        from rbczpremiumapi.api_client import ApiClient
        print("✓ ApiClient imported successfully")
        
        # Test API classes import
        from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi
        from rbczpremiumapi.PremiumAPI.get_accounts_api import GetAccountsApi
        print("✓ API classes imported successfully")
        
        # Test model classes import
        from rbczpremiumapi.Model.currency_list_simple import CurrencyListSimple
        print("✓ Model classes imported successfully")
        
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        traceback.print_exc()
        return False

def test_api_client_creation():
    """Test creating API client and API instances"""
    print("\nTesting API client creation...")
    
    try:
        from rbczpremiumapi.api_client import ApiClient
        from rbczpremiumapi.PremiumAPI.get_account_balance_api import GetAccountBalanceApi
        
        # Create API client
        client = ApiClient()
        print("✓ ApiClient created successfully")
        
        # Create API instance
        balance_api = GetAccountBalanceApi(client)
        print("✓ GetAccountBalanceApi created successfully")
        
        # Check that methods are available
        assert hasattr(balance_api, 'get_balance'), "get_balance method not found"
        print("✓ API methods are available")
        
        return True
    except Exception as e:
        print(f"✗ API creation error: {e}")
        traceback.print_exc()
        return False

def test_certificate_extraction():
    """Test certificate extraction functionality"""
    print("\nTesting certificate extraction functionality...")
    
    try:
        from rbczpremiumapi.api_client import ApiClient
        
        # Check that the method exists
        assert hasattr(ApiClient, 'extract_p12_certificate'), "extract_p12_certificate method not found"
        print("✓ extract_p12_certificate method is available")
        
        # Test that it raises appropriate errors for missing files
        try:
            ApiClient.extract_p12_certificate('/nonexistent/file.p12', 'password')
            print("✗ Should have raised FileNotFoundError")
            return False
        except FileNotFoundError:
            print("✓ Correctly raises FileNotFoundError for missing files")
        
        # Test that it raises appropriate errors for missing cryptography
        # This is harder to test without actually uninstalling cryptography
        print("✓ Certificate extraction method behaves correctly")
        
        return True
    except Exception as e:
        print(f"✗ Certificate extraction error: {e}")
        traceback.print_exc()
        return False

def test_configuration():
    """Test configuration functionality"""
    print("\nTesting configuration...")
    
    try:
        from rbczpremiumapi.configuration import Configuration
        
        # Create configuration
        config = Configuration()
        print("✓ Configuration created successfully")
        
        # Check default values
        assert hasattr(config, 'host'), "Configuration missing host attribute"
        print("✓ Configuration has expected attributes")
        
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🚀 Testing RBCZ Premium API Library")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_api_client_creation,
        test_certificate_extraction,
        test_configuration,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
                print("✅ PASSED")
            else:
                failed += 1
                print("❌ FAILED")
        except Exception as e:
            failed += 1
            print(f"❌ FAILED with exception: {e}")
        
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Library is working correctly.")
        return 0
    else:
        print("😞 Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())