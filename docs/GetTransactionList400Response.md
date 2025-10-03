# GetTransactionList400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Invalid date. Parameter &#x60;from&#x60; must not be older than 90 days. | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list400_response import GetTransactionList400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList400Response from a JSON string
get_transaction_list400_response_instance = GetTransactionList400Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList400Response.to_json())

# convert the object into a dict
get_transaction_list400_response_dict = get_transaction_list400_response_instance.to_dict()
# create an instance of GetTransactionList400Response from a dict
get_transaction_list400_response_from_dict = GetTransactionList400Response.from_dict(get_transaction_list400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


