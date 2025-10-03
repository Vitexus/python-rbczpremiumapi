# GetTransactionList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_page** | **bool** | Indication wheter the page is last - default false | [optional] 
**transactions** | [**List[GetTransactionList200ResponseTransactionsInner]**](GetTransactionList200ResponseTransactionsInner.md) | An array of transactions. | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response import GetTransactionList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200Response from a JSON string
get_transaction_list200_response_instance = GetTransactionList200Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200Response.to_json())

# convert the object into a dict
get_transaction_list200_response_dict = get_transaction_list200_response_instance.to_dict()
# create an instance of GetTransactionList200Response from a dict
get_transaction_list200_response_from_dict = GetTransactionList200Response.from_dict(get_transaction_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


