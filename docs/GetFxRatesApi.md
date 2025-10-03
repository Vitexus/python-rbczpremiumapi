# rbczpremiumapi.GetFxRatesApi

All URIs are relative to *https://api.rb.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fx_rates**](GetFxRatesApi.md#get_fx_rates) | **GET** /rbcz/premium/api/fxrates/{currencyCode} | 


# **get_fx_rates**
> CurrencyListSimple get_fx_rates(x_ibm_client_id, x_request_id, currency_code, psu_ip_address=psu_ip_address, var_date=var_date)

Returns foreign exchange rates for the given currency code.

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
    api_instance = rbczpremiumapi.GetFxRatesApi(api_client)
    x_ibm_client_id = 'x_ibm_client_id_example' # str | ClientID obtained from Developer Portal - when you registered your app with us.
    x_request_id = 'x_request_id_example' # str | Unique request id provided by consumer application for reference and auditing.
    currency_code = 'currency_code_example' # str | The foreign currency code in ISO-4217 format.
    psu_ip_address = 'psu_ip_address_example' # str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. (optional)
    var_date = '2013-10-20' # date | The effective date for which the FX rates are requested. Will default to **now** when not specified. (optional)

    try:
        api_response = api_instance.get_fx_rates(x_ibm_client_id, x_request_id, currency_code, psu_ip_address=psu_ip_address, var_date=var_date)
        print("The response of GetFxRatesApi->get_fx_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetFxRatesApi->get_fx_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. | 
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. | 
 **currency_code** | **str**| The foreign currency code in ISO-4217 format. | 
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional] 
 **var_date** | **date**| The effective date for which the FX rates are requested. Will default to **now** when not specified. | [optional] 

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
**200** | Foreign exchange rates for the given currency. |  -  |
**429** | User has sent too many requests in a given amount of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

