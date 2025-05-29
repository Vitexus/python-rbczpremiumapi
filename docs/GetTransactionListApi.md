# rbczpremiumapi\GetTransactionListApi

All URIs are relative to https://api.rb.cz.

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_list()**](GetTransactionListApi.md#get_transaction_list) | **GET** /rbcz/premium/api/accounts/{accountNumber}/{currencyCode}/transactions | 


## `get_transaction_list()`

```php
get_transaction_list($x_ibm_client_id, $x_request_id, $account_number, $currency_code, $var_from, $to, $psu_ip_address, $page): GetTransactionList200Response
```



Get a list of posted transactions (including intraday). In addition, transactions must not be older than **90 days** - see request parameter `from`.  The list is returned as a sequence of pages - see request parameter `page`. The request parameter/flag `lastPage` indicates whether the returned page is the last one or if there are more pages that you can iterate.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new rbczpremiumapi\Api\GetTransactionListApi(
    // If you want use custom http client, pass your client which implements `Psr\Http\Client\ClientInterface`.
    // This is optional, `Psr18ClientDiscovery` will be used to find http client. For instance `GuzzleHttp\Client` implements that interface
    new GuzzleHttp\Client()
);
$x_ibm_client_id = 'x_ibm_client_id_example'; // str | ClientID obtained from Developer Portal - when you registered your app with us.
$x_request_id = 'x_request_id_example'; // str | Unique request id provided by consumer application for reference and auditing.
$account_number = 'account_number_example'; // str | Account number for which to get list of transactions in national format without 0 padding.
$currency_code = 'currency_code_example'; // str | Currency code of the account in ISO-4217 standard (e.g. czk, eur, usd)
$var_from = '2013-10-20T19:20:30+01:00'; // datetime | Defines date (and optionally time) from which transactions will be requested. If no time is specified then 00:00:00.0 (Central European  Time) will be used. Example values - 2021-08-01 or 2021-08-01T10:00:00.0Z
$to = '2013-10-20T19:20:30+01:00'; // datetime | Defines date (and optionally time) until which transactions will be requested. If no time is specified then 23:59:59.999 (Central European  Time) will be used. Example values - 2021-08-02 or 2021-08-02T14:00:00.0Z
$psu_ip_address = 'psu_ip_address_example'; // str | IP address of a client - the end IP address of the client application (no server) in IPv4 or IPv6 format. If the bank client (your user) uses a browser by which he accesses your server app, we need to know the IP address of his browser. Always provide the closest IP address to the real end-user possible.
$page = 56; // int | Page number to be requested. The first page is 1.

try {
    $result = $apiInstance->get_transaction_list($x_ibm_client_id, $x_request_id, $account_number, $currency_code, $var_from, $to, $psu_ip_address, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GetTransactionListApi->get_transaction_list: ', $e->getMessage(), PHP_EOL;
}
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

[**GetTransactionList200Response**](../Model/GetTransactionList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
