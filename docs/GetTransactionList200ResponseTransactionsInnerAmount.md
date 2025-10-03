# GetTransactionList200ResponseTransactionsInnerAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Amount of money | 
**currency** | **str** | Currency code of the amount | 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_amount import GetTransactionList200ResponseTransactionsInnerAmount

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerAmount from a JSON string
get_transaction_list200_response_transactions_inner_amount_instance = GetTransactionList200ResponseTransactionsInnerAmount.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerAmount.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_amount_dict = get_transaction_list200_response_transactions_inner_amount_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerAmount from a dict
get_transaction_list200_response_transactions_inner_amount_from_dict = GetTransactionList200ResponseTransactionsInnerAmount.from_dict(get_transaction_list200_response_transactions_inner_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


