# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty

Information about counter party (debtor or creditor) - always the other side of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Bank account name | [optional] 
**postal_address** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyPostalAddress**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyPostalAddress.md) |  | [optional] 
**organisation_identification** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification.md) |  | [optional] 
**account** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyAccount.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterParty.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


