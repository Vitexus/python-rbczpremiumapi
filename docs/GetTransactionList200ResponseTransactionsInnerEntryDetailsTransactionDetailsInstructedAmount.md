# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount

Original amount in original currency - before currency conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Amount of money | 
**currency** | **str** | Currency code of the amount | 
**exchange_rate** | **float** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instructed_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


