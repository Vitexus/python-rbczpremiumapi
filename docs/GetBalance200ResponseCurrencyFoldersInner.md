# GetBalance200ResponseCurrencyFoldersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the currency folder | 
**status** | **str** | The status of the currency folder (CATALOG: CURRENCYFOLDERSTATUS) | 
**balances** | [**List[GetBalance200ResponseCurrencyFoldersInnerBalancesInner]**](GetBalance200ResponseCurrencyFoldersInnerBalancesInner.md) | the balances of the currencyFolder | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_balance200_response_currency_folders_inner import GetBalance200ResponseCurrencyFoldersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalance200ResponseCurrencyFoldersInner from a JSON string
get_balance200_response_currency_folders_inner_instance = GetBalance200ResponseCurrencyFoldersInner.from_json(json)
# print the JSON string representation of the object
print(GetBalance200ResponseCurrencyFoldersInner.to_json())

# convert the object into a dict
get_balance200_response_currency_folders_inner_dict = get_balance200_response_currency_folders_inner_instance.to_dict()
# create an instance of GetBalance200ResponseCurrencyFoldersInner from a dict
get_balance200_response_currency_folders_inner_from_dict = GetBalance200ResponseCurrencyFoldersInner.from_dict(get_balance200_response_currency_folders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


