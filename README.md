# RBCZ Premium API Library

This library provides a Python interface to the Raiffeisenbank CZ Premium API.

## API Documentation

##### API Overview
- Accounts list and balance
- Transaction overview (also for saving accounts)
- Payments import
- Statement list and download
- FX rates

##### Authentication
Before making a call to Premium API, you need to register your app at our _Developer portal_. This is where you get the **ClientID** that your application must send in the request as `X-IBM-Client-Id`. This is the key that grants your app access to the API.

However, this may not be enough. Your application needs to use mTLS to call most operations here. Thus, you not only need _https_ but also a client certificate issued by us. The exception is two operations for FX rates that are accessible also without a client certificate.

Each bank client/user can issue several certificates. Each certificate can permit different sets of operations (http methods) on different bank accounts. All this must be configured in Internet Banking first by each bank client/user (bank clients need to look under _Settings_ and do not forget to download the certificate at the last step). The certificate is downloaded in **PKCS#12** format as **\*.p12** file and protected by a password chosen by the bank client/user. Yes, your app needs the password as well to get use of the **\*p12** file for establishing mTLS connection to the bank.

Client certificates issued in Internet Banking for bank clients/users have limited validity (e.g. **5 years**). However, **each year** certificates are automatically blocked and bank client/user must unblock them in Internet Banking. It is possible to do it in advance and prolong the time before the certificate is blocked. Your app should be prepared for these scenarios and it should communicate such cases to your user in advance to provide seamless service and high user-experience of your app.

For testing purposes please download and use our <a href="https://developers.rb.cz/premium/assets/test_cert.p12" download> test client certificate</a>. The certificate password is <i>Test12345678</i>.

##### Rate Limiting
In production environment the request rate is limited according to your subscription plan. Therefore the consumer must be able to handle HTTP responses status 429 in case of exceeding these limits.

Response headers `X-RateLimit-Limit-Second` and `X-RateLimit-Limit-Day` show the actual limits configured for the specific operation. Response headers `X-RateLimit-Remaining-Second` and `X-RateLimit-Remaining-Day` are returned to help prevent the limits from being exceeded.

##### Notes
Be aware, that in certain error situations, API can return specific error structures along with 5xx status code, which is not explicitely defined below.

## Installation

Install the library using pip:

```bash
pip install rbczpremiumapi
```

## Usage

```python
from rbczpremiumapi import PremiumAPI

# Initialize the API client
client = PremiumAPI(
    client_id='your_client_id',
    p12_path='path/to/your/certificate.p12',
    p12_password='your_certificate_password'
)

# Fetch account details
accounts = client.get_accounts()
print(accounts)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
