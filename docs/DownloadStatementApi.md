# rbczpremiumapi\DownloadStatementApi

All URIs are relative to https://api.rb.cz.

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_statement()**](DownloadStatementApi.md#download_statement) | **POST** /rbcz/premium/api/accounts/statements/download | 


## `download_statement()`

```php
download_statement($x_ibm_client_id, $x_request_id, $accept_language, $request_body, $psu_ip_address): bytearray
```



Download the selected statement.  Returns one of the following `Content-type` header values depending on  the downloaded document type: <code>application/pdf</code>, <code>application/xml</code>, <code>text/mt940</code>, <code>application/json</code> (in case of an error). 

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new rbczpremiumapi\Api\DownloadStatementApi(
    // If you want use custom http client, pass your client which implements `Psr\Http\Client\ClientInterface`.
    // This is optional, `Psr18ClientDiscovery` will be used to find http client. For instance `GuzzleHttp\Client` implements that interface
    new GuzzleHttp\Client()
);
$x_ibm_client_id = 'x_ibm_client_id_example'; // str | ClientID obtained from Developer Portal - when you registered your app with us.
$x_request_id = 'x_request_id_example'; // str | Unique request id provided by consumer application for reference and auditing.
$accept_language = 'accept_language_example'; // str | The Accept-Language request HTTP header is used to determine document  language. Supported languages are `cs` and `en`.
$request_body = rbczpremiumapi.DownloadStatementRequest(); // DownloadStatementRequest
$psu_ip_address = 'psu_ip_address_example'; // str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible.

try {
    $result = $apiInstance->download_statement($x_ibm_client_id, $x_request_id, $accept_language, $request_body, $psu_ip_address);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DownloadStatementApi->download_statement: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. |
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. |
 **accept_language** | **str**| The Accept-Language request HTTP header is used to determine document  language. Supported languages are &#x60;cs&#x60; and &#x60;en&#x60;. |
 **request_body** | [**DownloadStatementRequest**](../Model/DownloadStatementRequest.md)|  |
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `*/*`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
