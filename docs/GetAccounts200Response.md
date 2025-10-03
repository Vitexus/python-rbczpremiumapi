# GetAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[GetAccounts200ResponseAccountsInner]**](GetAccounts200ResponseAccountsInner.md) | An array of accounts. | [optional] 
**page** | **int** | actual returned page | [optional] 
**size** | **int** | Number of items on the page | [optional] 
**first** | **bool** | true for first page | [optional] 
**last** | **bool** | true for last page | [optional] 
**total_pages** | **int** | total number of pages | [optional] 
**total_size** | **int** | total number of items | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_accounts200_response import GetAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccounts200Response from a JSON string
get_accounts200_response_instance = GetAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccounts200Response.to_json())

# convert the object into a dict
get_accounts200_response_dict = get_accounts200_response_instance.to_dict()
# create an instance of GetAccounts200Response from a dict
get_accounts200_response_from_dict = GetAccounts200Response.from_dict(get_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


