# GetTransactionList200ResponseTransactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_reference** | **str** | Unique identification of the realized transaction. | 
**amount** | [**GetTransactionList200ResponseTransactionsInnerAmount**](GetTransactionList200ResponseTransactionsInnerAmount.md) |  | 
**credit_debit_indication** | **str** |  | 
**booking_date** | **datetime** | Date of payment processing/posting by the bank. | [optional] 
**value_date** | **datetime** | Transaction date; value date; date which is used to count interest; e.g. date when money were withdrawn from ATM. | [optional] 
**bank_transaction_code** | [**GetTransactionList200ResponseTransactionsInnerBankTransactionCode**](GetTransactionList200ResponseTransactionsInnerBankTransactionCode.md) |  | 
**entry_details** | [**GetTransactionList200ResponseTransactionsInnerEntryDetails**](GetTransactionList200ResponseTransactionsInnerEntryDetails.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner import GetTransactionList200ResponseTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInner from a JSON string
get_transaction_list200_response_transactions_inner_instance = GetTransactionList200ResponseTransactionsInner.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInner.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_dict = get_transaction_list200_response_transactions_inner_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInner from a dict
get_transaction_list200_response_transactions_inner_from_dict = GetTransactionList200ResponseTransactionsInner.from_dict(get_transaction_list200_response_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


