import os
import tempfile
import requests
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, PrivateFormat, NoEncryption

class PremiumAPI:
    """
    A client for the Raiffeisenbank CZ Premium API.
    """
    def __init__(self, client_id, p12_path, p12_password, sandbox=True):
        self.client_id = client_id
        self.p12_path = p12_path
        self.p12_password = p12_password
        self.sandbox = sandbox
        self.base_url = "https://api.rb.cz/rbcz/premium/mock" if sandbox else "https://api.rb.cz/rbcz/premium/api"

        self.cert_file = None
        self.key_file = None
        self._extract_p12()

    def _extract_p12(self):
        """
        Extracts the certificate and private key from a .p12 file.
        """
        with open(self.p12_path, "rb") as f:
            p12_data = f.read()

        private_key, certificate, _ = pkcs12.load_key_and_certificates(
            p12_data,
            self.p12_password.encode()
        )

        cert_pem = certificate.public_bytes(Encoding.PEM)
        key_pem = private_key.private_bytes(
            Encoding.PEM,
            PrivateFormat.PKCS8,
            NoEncryption()
        )

        cert_file_h, self.cert_file = tempfile.mkstemp(suffix=".pem")
        key_file_h, self.key_file = tempfile.mkstemp(suffix=".pem")

        with os.fdopen(cert_file_h, 'w') as f:
            f.write(cert_pem.decode())

        with os.fdopen(key_file_h, 'w') as f:
            f.write(key_pem.decode())

    def __del__(self):
        """
        Cleans up the temporary certificate and key files.
        """
        if self.cert_file:
            os.unlink(self.cert_file)
        if self.key_file:
            os.unlink(self.key_file)

    def _request(self, method, endpoint, **kwargs):
        """
        Makes a request to the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'X-IBM-Client-Id': self.client_id,
            'X-Request-Id': 'some-random-string', # This should be a unique id
        }

        response = requests.request(
            method,
            url,
            headers=headers,
            cert=(self.cert_file, self.key_file),
            **kwargs
        )
        response.raise_for_status()
        return response.json()

    def get_accounts(self):
        """
        Fetches the list of accounts.
        """
        return self._request('GET', 'accounts')

    def get_balance(self, account_number):
        """
        Fetches the balance for a given account.
        """
        return self._request('GET', f'accounts/{account_number}/balance')

    def get_transaction_list(self, account_number, currency_code, params=None):
        """
        Fetches the list of transactions for a given account.
        """
        return self._request('GET', f'accounts/{account_number}/{currency_code}/transactions', params=params)
