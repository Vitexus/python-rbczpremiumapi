# GetTransactionList200ResponseTransactionsInnerBankTransactionCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Transaction code in ISO20022 camt.53 format (e.g. 10000101000 - Odchozi tuzemska platba). | 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_bank_transaction_code import GetTransactionList200ResponseTransactionsInnerBankTransactionCode

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerBankTransactionCode from a JSON string
get_transaction_list200_response_transactions_inner_bank_transaction_code_instance = GetTransactionList200ResponseTransactionsInnerBankTransactionCode.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerBankTransactionCode.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_bank_transaction_code_dict = get_transaction_list200_response_transactions_inner_bank_transaction_code_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerBankTransactionCode from a dict
get_transaction_list200_response_transactions_inner_bank_transaction_code_from_dict = GetTransactionList200ResponseTransactionsInnerBankTransactionCode.from_dict(get_transaction_list200_response_transactions_inner_bank_transaction_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


