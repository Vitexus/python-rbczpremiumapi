# rbczpremiumapi\GetFxRatesApi

All URIs are relative to https://api.rb.cz.

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fx_rates()**](GetFxRatesApi.md#get_fx_rates) | **GET** /rbcz/premium/api/fxrates/{currencyCode} | 


## `get_fx_rates()`

```php
get_fx_rates($x_ibm_client_id, $x_request_id, $currency_code, $psu_ip_address, $var_date): CurrencyListSimple
```



Returns foreign exchange rates for the given currency code.  This operation does not require a client certificate. 

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new rbczpremiumapi\Api\GetFxRatesApi(
    // If you want use custom http client, pass your client which implements `Psr\Http\Client\ClientInterface`.
    // This is optional, `Psr18ClientDiscovery` will be used to find http client. For instance `GuzzleHttp\Client` implements that interface
    new GuzzleHttp\Client()
);
$x_ibm_client_id = 'x_ibm_client_id_example'; // str | ClientID obtained from Developer Portal - when you registered your app with us.
$x_request_id = 'x_request_id_example'; // str | Unique request id provided by consumer application for reference and auditing.
$currency_code = 'currency_code_example'; // str | The foreign currency code in ISO-4217 format.
$psu_ip_address = 'psu_ip_address_example'; // str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible.
$var_date = '2013-10-20'; // date | The effective date for which the FX rates are requested. Will default to **now** when not specified.

try {
    $result = $apiInstance->get_fx_rates($x_ibm_client_id, $x_request_id, $currency_code, $psu_ip_address, $var_date);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GetFxRatesApi->get_fx_rates: ', $e->getMessage(), PHP_EOL;
}
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

[**CurrencyListSimple**](../Model/CurrencyListSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
