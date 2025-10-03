# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**bic_or_bei** | **str** | SWIFT/BIC code of the bank. | [optional] 
**bank_code** | **str** | Proprietary bank code in local format (e.g. 5500) or in foreign format. | [optional] 
**postal_address** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitutionPostalAddress**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitutionPostalAddress.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedPartiesIntermediaryInstitution.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_related_parties_intermediary_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


