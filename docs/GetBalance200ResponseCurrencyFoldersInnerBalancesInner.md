# GetBalance200ResponseCurrencyFoldersInnerBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_type** | **str** | the balance type (CODEBOOK: AccountBalanceTypes) | 
**currency** | **str** | The currency of the balance | 
**value** | **float** | The balance amount | 

## Example

```python
from rbczpremiumapi.Model.get_balance200_response_currency_folders_inner_balances_inner import GetBalance200ResponseCurrencyFoldersInnerBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalance200ResponseCurrencyFoldersInnerBalancesInner from a JSON string
get_balance200_response_currency_folders_inner_balances_inner_instance = GetBalance200ResponseCurrencyFoldersInnerBalancesInner.from_json(json)
# print the JSON string representation of the object
print(GetBalance200ResponseCurrencyFoldersInnerBalancesInner.to_json())

# convert the object into a dict
get_balance200_response_currency_folders_inner_balances_inner_dict = get_balance200_response_currency_folders_inner_balances_inner_instance.to_dict()
# create an instance of GetBalance200ResponseCurrencyFoldersInnerBalancesInner from a dict
get_balance200_response_currency_folders_inner_balances_inner_from_dict = GetBalance200ResponseCurrencyFoldersInnerBalancesInner.from_dict(get_balance200_response_currency_folders_inner_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


