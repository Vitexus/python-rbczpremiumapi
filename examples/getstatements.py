import os
import requests

# Initialize environment variables
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')

# Example function to fetch statements
def get_statements():
    url = "https://api.raiffeisenbank.cz/premium/statements"
    headers = {
        "X-IBM-Client-Id": X_IBM_CLIENT_ID,
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Statements fetched successfully:", response.json())
    else:
        print("Failed to fetch statements:", response.status_code, response.text)

if __name__ == "__main__":
    get_statements()
