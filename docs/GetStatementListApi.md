# rbczpremiumapi.GetStatementListApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statements**](GetStatementListApi.md#get_statements) | **POST** /rbcz/premium/api/accounts/statements | 


# **get_statements**
> GetStatements200Response get_statements(x_ibm_client_id, x_request_id, request_body, psu_ip_address=psu_ip_address, page=page, size=size)

Lists statements for all available accounts for which the client has appropriate access rights.


### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.get_statements200_response import GetStatements200Response
from rbczpremiumapi.models.get_statements_request import GetStatementsRequest
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
    api_instance = rbczpremiumapi.GetStatementListApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    request_body = rbczpremiumapi.GetStatementsRequest() # GetStatementsRequest | 
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)
    page = 56 # int | Number of the requested page. Default is 1. (optional)
    size = 56 # int | Number of items on the page. Default is 15. (optional)

    try:
        api_response = api_instance.get_statements(x_ibm_client_id, x_request_id, request_body, psu_ip_address=psu_ip_address, page=page, size=size)
        print("The response of GetStatementListApi->get_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetStatementListApi->get_statements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **request_body** | [**GetStatementsRequest**](GetStatementsRequest.md)|  | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 
 **page** | **int**| Number of the requested page. Default is 1. | [optional] 
 **size** | **int**| Number of items on the page. Default is 15. | [optional] 

### Return type

[**GetStatements200Response**](GetStatements200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | Nonexisting page or empty content.  |  -  |
**400** | Bad request, validation error. |  -  |
**401** | Certificate is invalid. |  -  |
**403** | No access rights to perform the operation. |  -  |
**404** | Indicates that requested resource does not exist. |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

