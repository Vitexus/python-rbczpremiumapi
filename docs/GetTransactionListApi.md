# rbczpremiumapi.GetTransactionListApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_list**](GetTransactionListApi.md#get_transaction_list) | **GET** /rbcz/premium/api/accounts/{accountNumber}/{currencyCode}/transactions | 


# **get_transaction_list**
> GetTransactionList200Response get_transaction_list(x_ibm_client_id, x_request_id, account_number, currency_code, var_from, to, psu_ip_address=psu_ip_address, page=page)

Get a list of posted transactions (including intraday). In addition, transactions must not be older than **90 days** - see request parameter `from`.

The list is returned as a sequence of pages - see request parameter `page`. The request parameter/flag `lastPage` indicates whether the returned page is the last one or if there are more pages that you can iterate.

### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.get_transaction_list200_response import GetTransactionList200Response
from rbczpremiumapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rb.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = rbczpremiumapi.Configuration(
    host = "https://api.rb.cz"
)


# Enter a context with an instance of the API client
with rbczpremiumapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rbczpremiumapi.GetTransactionListApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    account_number = 'account_number_example' # str | Account number for which to get list of transactions in national format without 0 padding.
    currency_code = 'currency_code_example' # str | Currency code of the account in ISO-4217 standard (e.g. czk, eur, usd)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Defines date (and optionally time) from which transactions will be requested. If no time is specified then 00:00:00.0 (Central European  Time) will be used. Example values - 2021-08-01 or 2021-08-01T10:00:00.0Z
    to = '2013-10-20T19:20:30+01:00' # datetime | Defines date (and optionally time) until which transactions will be requested. If no time is specified then 23:59:59.999 (Central European  Time) will be used. Example values - 2021-08-02 or 2021-08-02T14:00:00.0Z
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)
    page = 56 # int | Page number to be requested. The first page is 1. (optional)

    try:
        api_response = api_instance.get_transaction_list(x_ibm_client_id, x_request_id, account_number, currency_code, var_from, to, psu_ip_address=psu_ip_address, page=page)
        print("The response of GetTransactionListApi->get_transaction_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetTransactionListApi->get_transaction_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **account_number** | **str**| Account number for which to get list of transactions in national format without 0 padding. | 
 **currency_code** | **str**| Currency code of the account in ISO-4217 standard (e.g. czk, eur, usd) | 
 **var_from** | **datetime**| Defines date (and optionally time) from which transactions will be requested. If no time is specified then 00:00:00.0 (Central European  Time) will be used. Example values - 2021-08-01 or 2021-08-01T10:00:00.0Z | 
 **to** | **datetime**| Defines date (and optionally time) until which transactions will be requested. If no time is specified then 23:59:59.999 (Central European  Time) will be used. Example values - 2021-08-02 or 2021-08-02T14:00:00.0Z | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 
 **page** | **int**| Page number to be requested. The first page is 1. | [optional] 

### Return type

[**GetTransactionList200Response**](GetTransactionList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | Nonexisting page or empty content.  |  -  |
**400** | Bad request, validation error. |  -  |
**401** | Certificate is invalid. |  -  |
**403** | No access rights to perform the operation. |  -  |
**404** |  |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

