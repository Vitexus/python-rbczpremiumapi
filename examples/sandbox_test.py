import os
from dotenv import load_dotenv
from rbczpremiumapi import PremiumAPI

def main():
    """
    Main function to test the API.
    """
    load_dotenv(dotenv_path='examples/example.env')

    client_id = os.getenv('XIBMCLIENTID')
    p12_path = os.getenv('CERT_FILE')
    p12_password = os.getenv('CERT_PASS')

    if not all([client_id, p12_path, p12_password]):
        print("Error: Make sure XIBMCLIENTID, CERT_FILE, and CERT_PASS are set in examples/example.env")
        return

    # Adjust p12_path to be relative to the examples directory
    p12_path = os.path.join('examples', p12_path)

    try:
        client = PremiumAPI(
            client_id=client_id,
            p12_path=p12_path,
            p12_password=p12_password
        )

        print("Fetching accounts...")
        accounts = client.get_accounts()
        print("Successfully fetched accounts:")
        print(accounts)

        if accounts and accounts.get('accounts'):
            account_number = accounts['accounts'][0]['accountNumber']
            print(f"\nFetching balance for account {account_number}...")
            balance = client.get_balance(account_number)
            print("Successfully fetched balance:")
            print(balance)

            from datetime import datetime, timedelta

            print(f"\nFetching transactions for account {account_number}...")
            # Get transactions from the last 30 days
            to_date = datetime.now()
            from_date = to_date - timedelta(days=30)

            transactions = client.get_transaction_list(
                account_number,
                'CZK',
                params={
                    'from': from_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    'to': to_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                }
            )
            print("Successfully fetched transactions:")
            print(transactions)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
