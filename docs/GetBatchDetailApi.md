# rbczpremiumapi.GetBatchDetailApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_detail**](GetBatchDetailApi.md#get_batch_detail) | **GET** /rbcz/premium/api/payments/batches/{batchFileId} | 


# **get_batch_detail**
> GetBatchDetail200Response get_batch_detail(x_ibm_client_id, x_request_id, batch_file_id, psu_ip_address=psu_ip_address)

Getting details about state of processing of imported batch file and created batch transactions.

All possible batch `status` values are: DRAFT, ERROR, FOR_SIGN, VERIFIED, PASSING_TO_BANK, PASSED, PASSED_TO_BANK_WITH_ERROR, UNDISCLOSED

### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.get_batch_detail200_response import GetBatchDetail200Response
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
    api_instance = rbczpremiumapi.GetBatchDetailApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    batch_file_id = 56 # int | Batch file id 
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)

    try:
        api_response = api_instance.get_batch_detail(x_ibm_client_id, x_request_id, batch_file_id, psu_ip_address=psu_ip_address)
        print("The response of GetBatchDetailApi->get_batch_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetBatchDetailApi->get_batch_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **batch_file_id** | **int**| Batch file id  | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 

### Return type

[**GetBatchDetail200Response**](GetBatchDetail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch payment detail. |  -  |
**400** | Bad request, validation error. |  -  |
**401** | Certificate is invalid. |  -  |
**403** | No access rights to perform the operation. |  -  |
**404** |  |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

