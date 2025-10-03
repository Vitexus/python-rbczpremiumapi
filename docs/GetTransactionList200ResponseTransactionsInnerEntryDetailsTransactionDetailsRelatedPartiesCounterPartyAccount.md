# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **str** | IBAN code of the bank account if available | [optional] 
**account_number_prefix** | **str** | Prefix part of the bank account number (only for czech accounts) | [optional] 
**account_number** | **str** | Base part of the bank account number in czech fromat or in foreign format | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


