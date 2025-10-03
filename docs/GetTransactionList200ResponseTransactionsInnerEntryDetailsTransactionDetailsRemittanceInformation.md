# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation

Information that allow match and pairing transactions or further identifies it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Information from or for counter party. Information for creditor. | [optional] 
**creditor_reference_information** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformationCreditorReferenceInformation**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformationCreditorReferenceInformation.md) |  | [optional] 
**originator_message** | **str** | Private description of the transaction. Only available to account holder. | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_remittance_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


