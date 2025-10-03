# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**bic_or_bei** | **str** | SWIFT/BIC code of the bank. | [optional] 
**bank_code** | **str** | Proprietary bank code in local format (e.g. 5500) or in foreign format. | [optional] 
**postal_address** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentificationPostalAddress**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentificationPostalAddress.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesCounterPartyOrganisationIdentification.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_counter_party_organisation_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


