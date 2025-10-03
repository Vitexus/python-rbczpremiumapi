# rbczpremiumapi.UploadPaymentsApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_payments**](UploadPaymentsApi.md#import_payments) | **POST** /rbcz/premium/api/payments/batches | 


# **import_payments**
> ImportPayments200Response import_payments(x_ibm_client_id, x_request_id, batch_import_format, request_body, psu_ip_address=psu_ip_address, batch_name=batch_name, batch_combined_payments=batch_combined_payments, batch_autocorrect=batch_autocorrect)

Importing batch payments in one of [supported formates](https://www.rb.cz/attachments/direct-banking/ekomunikator-datova-struktura.pdf) - see request parameter `Batch-Import-Format`.

This is an API alternative to the manual import of batch payments through [Internet Banking](https://www.rb.cz/podnikatele/ucty-a-platebni-styk/prime-bankovnictvi/internetove-bankovnictvi/caste-dotazy/import-hromadnych-plateb).

Imported payments are not immediately processed, they are just loaded into Internet Banking and they still must be authorized/certified in Internet Banking according to client settings of disposable rights and signatures.

Once authorized/certified, uploaded payments will be processed in the Instant payments mode if the following conditions are met&#58;
1. the batch has no more than 100 payments
2. no more than 10 batches per day were uploaded
3. individual payments meet the conditions for Instant payments - see [Instant Payments](https://www.rb.cz/informacni-servis/platebni-styk/tuzemske-platby/okamzite-platby)
4. on the weekend, only payments within our bank are processed as Instant payments

The number of transactions in one request is limited to 15.000 (this can change without prior notice). The limit is not checked during the call,  it is performed later and a possible error is provided in Internet Banking.

### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.import_payments200_response import ImportPayments200Response
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
    api_instance = rbczpremiumapi.UploadPaymentsApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    batch_import_format = 'batch_import_format_example' # str | Format of imported batch. For CCT format please use option SEPA-XML.
    request_body = 'request_body_example' # str | 
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)
    batch_name = 'batch_name_example' # str | Batch name, if not present then will be generated in format `ImportApi_<DDMMYYYY>`.  If the name is longer than 50 characters, it will be truncated   (optional)
    batch_combined_payments = False # bool | Optional header for combined payments. Payments inside the import file are considered as combined in case the header is present and its value is set to 'true'.  (optional) (default to False)
    batch_autocorrect = True # bool | Flag if valueDate should be autocorrected in the imported file or not. Autocorrection moved valueDate on first available valid  (working) day. Beware that this may affect if the payment will be sent as instant or not since only payments with valueDate same as actual date (during sending of payment to bank) can be sent as instant.  (optional) (default to True)

    try:
        api_response = api_instance.import_payments(x_ibm_client_id, x_request_id, batch_import_format, request_body, psu_ip_address=psu_ip_address, batch_name=batch_name, batch_combined_payments=batch_combined_payments, batch_autocorrect=batch_autocorrect)
        print("The response of UploadPaymentsApi->import_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadPaymentsApi->import_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **batch_import_format** | **str**| Format of imported batch. For CCT format please use option SEPA-XML. | 
 **request_body** | **str**|  | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 
 **batch_name** | **str**| Batch name, if not present then will be generated in format &#x60;ImportApi_&lt;DDMMYYYY&gt;&#x60;.  If the name is longer than 50 characters, it will be truncated   | [optional] 
 **batch_combined_payments** | **bool**| Optional header for combined payments. Payments inside the import file are considered as combined in case the header is present and its value is set to &#39;true&#39;.  | [optional] [default to False]
 **batch_autocorrect** | **bool**| Flag if valueDate should be autocorrected in the imported file or not. Autocorrection moved valueDate on first available valid  (working) day. Beware that this may affect if the payment will be sent as instant or not since only payments with valueDate same as actual date (during sending of payment to bank) can be sent as instant.  | [optional] [default to True]

### Return type

[**ImportPayments200Response**](ImportPayments200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New batch with payments created |  -  |
**400** | Bad request, validation error. |  -  |
**401** | Certificate is invalid. |  -  |
**403** | No access rights to perform the operation. |  -  |
**413** | Indicates that the request payload is too large |  -  |
**415** | Unsupported media type |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

