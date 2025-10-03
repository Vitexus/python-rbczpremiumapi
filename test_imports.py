#!/usr/bin/env python3
"""
Test library imports
"""

try:
    from rbczpremiumapi import GetAccountsApi, Configuration, ApiClient
    print("✅ Library imports work!")
except ImportError as e:
    print(f"❌ Import failed: {e}")