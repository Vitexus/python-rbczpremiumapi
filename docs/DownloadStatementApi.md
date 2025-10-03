# rbczpremiumapi.DownloadStatementApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_statement**](DownloadStatementApi.md#download_statement) | **POST** /rbcz/premium/api/accounts/statements/download | 


# **download_statement**
> bytearray download_statement(x_ibm_client_id, x_request_id, accept_language, request_body, psu_ip_address=psu_ip_address)

Download the selected statement.

Returns one of the following `Content-type` header values depending on  the downloaded document type: <code>application/pdf</code>, <code>application/xml</code>, <code>text/mt940</code>, <code>application/json</code> (in case of an error).


### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.download_statement_request import DownloadStatementRequest
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
    api_instance = rbczpremiumapi.DownloadStatementApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    accept_language = 'accept_language_example' # str | The Accept-Language request HTTP header is used to determine document  language. Supported languages are `cs` and `en`.
    request_body = rbczpremiumapi.DownloadStatementRequest() # DownloadStatementRequest | 
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)

    try:
        api_response = api_instance.download_statement(x_ibm_client_id, x_request_id, accept_language, request_body, psu_ip_address=psu_ip_address)
        print("The response of DownloadStatementApi->download_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadStatementApi->download_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **accept_language** | **str**| The Accept-Language request HTTP header is used to determine document  language. Supported languages are &#x60;cs&#x60; and &#x60;en&#x60;. | 
 **request_body** | [**DownloadStatementRequest**](DownloadStatementRequest.md)|  | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document present and ready for download. |  -  |
**204** | Nonexisting page or empty content. |  -  |
**400** | Bad request, validation error. |  -  |
**401** | Certificate is invalid. |  -  |
**403** | No access rights to perform the operation. |  -  |
**404** | Indicates that requested resource does not exist. |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

