# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_party** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty.md) |  | [optional] 
**intermediary_institution** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution.md) |  | [optional] 
**ultimate_counter_party** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesUltimateCounterParty**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesUltimateCounterParty.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


