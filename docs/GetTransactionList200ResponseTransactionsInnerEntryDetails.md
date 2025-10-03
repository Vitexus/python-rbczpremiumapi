# GetTransactionList200ResponseTransactionsInnerEntryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_details** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details import GetTransactionList200ResponseTransactionsInnerEntryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetails from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_instance = GetTransactionList200ResponseTransactionsInnerEntryDetails.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetails.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_dict = get_transaction_list200_response_transactions_inner_entry_details_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetails from a dict
get_transaction_list200_response_transactions_inner_entry_details_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetails.from_dict(get_transaction_list200_response_transactions_inner_entry_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


