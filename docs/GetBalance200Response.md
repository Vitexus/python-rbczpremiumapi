# GetBalance200Response

Account with balances

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_part1** | **str** | The prefix of the account number | [optional] 
**number_part2** | **str** | The account number without prefix | 
**bank_code** | **str** | The bank clearing code | 
**currency_folders** | [**List[GetBalance200ResponseCurrencyFoldersInner]**](GetBalance200ResponseCurrencyFoldersInner.md) | The available currency folders information. | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_balance200_response import GetBalance200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalance200Response from a JSON string
get_balance200_response_instance = GetBalance200Response.from_json(json)
# print the JSON string representation of the object
print(GetBalance200Response.to_json())

# convert the object into a dict
get_balance200_response_dict = get_balance200_response_instance.to_dict()
# create an instance of GetBalance200Response from a dict
get_balance200_response_from_dict = GetBalance200Response.from_dict(get_balance200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


