# GetAccounts200ResponseAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The unique internal account id | 
**account_name** | **str** | The account name | [optional] 
**friendly_name** | **str** | The account nick name | [optional] 
**account_number** | **str** | The account number without prefix | 
**account_number_prefix** | **str** | The account number prefix | [optional] 
**iban** | **str** | The account number in IBAN format | [optional] 
**bank_code** | **str** | The bank clearing code | 
**bank_bic_code** | **str** | The bank BIC (SWIFT) code | [optional] 
**main_currency** | **str** | The main currency of the account | [optional] 
**account_type_id** | **str** | The account type | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_accounts200_response_accounts_inner import GetAccounts200ResponseAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccounts200ResponseAccountsInner from a JSON string
get_accounts200_response_accounts_inner_instance = GetAccounts200ResponseAccountsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccounts200ResponseAccountsInner.to_json())

# convert the object into a dict
get_accounts200_response_accounts_inner_dict = get_accounts200_response_accounts_inner_instance.to_dict()
# create an instance of GetAccounts200ResponseAccountsInner from a dict
get_accounts200_response_accounts_inner_from_dict = GetAccounts200ResponseAccountsInner.from_dict(get_accounts200_response_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


