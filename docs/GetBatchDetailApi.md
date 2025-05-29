# rbczpremiumapi\GetBatchDetailApi

All URIs are relative to https://api.rb.cz.

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_detail()**](GetBatchDetailApi.md#get_batch_detail) | **GET** /rbcz/premium/api/payments/batches/{batchFileId} | 


## `get_batch_detail()`

```php
get_batch_detail($x_ibm_client_id, $x_request_id, $batch_file_id, $psu_ip_address): GetBatchDetail200Response
```



Getting details about state of processing of imported batch file and created batch transactions.  All possible batch `status` values are: DRAFT, ERROR, FOR_SIGN, VERIFIED, PASSING_TO_BANK, PASSED, PASSED_TO_BANK_WITH_ERROR, UNDISCLOSED

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new rbczpremiumapi\Api\GetBatchDetailApi(
    // If you want use custom http client, pass your client which implements `Psr\Http\Client\ClientInterface`.
    // This is optional, `Psr18ClientDiscovery` will be used to find http client. For instance `GuzzleHttp\Client` implements that interface
    new GuzzleHttp\Client()
);
$x_ibm_client_id = 'x_ibm_client_id_example'; // str | ClientID obtained from Developer Portal - when you registered your app with us.
$x_request_id = 'x_request_id_example'; // str | Unique request id provided by consumer application for reference and auditing.
$batch_file_id = 56; // int | Batch file id 
$psu_ip_address = 'psu_ip_address_example'; // str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible.

try {
    $result = $apiInstance->get_batch_detail($x_ibm_client_id, $x_request_id, $batch_file_id, $psu_ip_address);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GetBatchDetailApi->get_batch_detail: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ibm_client_id** | **str**| ClientID obtained from Developer Portal - when you registered your app with us. |
 **x_request_id** | **str**| Unique request id provided by consumer application for reference and auditing. |
 **batch_file_id** | **int**| Batch file id  |
 **psu_ip_address** | **str**| IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible. | [optional]

### Return type

[**GetBatchDetail200Response**](../Model/GetBatchDetail200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
