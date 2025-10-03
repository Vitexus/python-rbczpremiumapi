# rbczpremiumapi.GetFxRatesListApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fx_rates_list**](GetFxRatesListApi.md#get_fx_rates_list) | **GET** /rbcz/premium/api/fxrates | 


# **get_fx_rates_list**
> CurrencyListSimple get_fx_rates_list(x_ibm_client_id, x_request_id, psu_ip_address=psu_ip_address, var_date=var_date)

Returns foreign exchange rates for all available currencies.

This operation does not require a client certificate.


### Example


```python
import rbczpremiumapi
from rbczpremiumapi.models.currency_list_simple import CurrencyListSimple
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
    api_instance = rbczpremiumapi.GetFxRatesListApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)
    var_date = '2013-10-20' # date | The effective date for which the FX rates list is requested. Will default to **now** when not specified. (optional)

    try:
        api_response = api_instance.get_fx_rates_list(x_ibm_client_id, x_request_id, psu_ip_address=psu_ip_address, var_date=var_date)
        print("The response of GetFxRatesListApi->get_fx_rates_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetFxRatesListApi->get_fx_rates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 
 **var_date** | **date**| The effective date for which the FX rates list is requested. Will default to **now** when not specified. | [optional] 

### Return type

[**CurrencyListSimple**](CurrencyListSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foreign exchange rates for all available currencies. |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

