import os
import requests

# Initialize environment variables
X_IBM_CLIENT_ID = os.getenv('XIBMCLIENTID')

# Example function to download statements
def download_statements():
    url = "https://api.raiffeisenbank.cz/premium/statements/download"
    headers = {
        "X-IBM-Client-Id": X_IBM_CLIENT_ID,
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("statements.zip", "wb") as file:
            file.write(response.content)
        print("Statements downloaded successfully.")
    else:
        print("Failed to download statements:", response.status_code, response.text)

if __name__ == "__main__":
    download_statements()
