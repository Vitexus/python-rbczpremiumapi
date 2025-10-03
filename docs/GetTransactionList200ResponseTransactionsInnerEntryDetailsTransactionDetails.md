# GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**references** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsReferences**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsReferences.md) |  | [optional] 
**instructed_amount** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsInstructedAmount.md) |  | [optional] 
**charge_bearer** | **str** |  | [optional] 
**payment_card_number** | **str** | Masked payment card number, if the transaction is related to debit card. | [optional] 
**related_parties** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRelatedParties.md) |  | [optional] 
**remittance_information** | [**GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation**](GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetailsRemittanceInformation.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_transaction_list200_response_transactions_inner_entry_details_transaction_details import GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails from a JSON string
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instance = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails.from_json(json)
# print the JSON string representation of the object
print(GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails.to_json())

# convert the object into a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_dict = get_transaction_list200_response_transactions_inner_entry_details_transaction_details_instance.to_dict()
# create an instance of GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails from a dict
get_transaction_list200_response_transactions_inner_entry_details_transaction_details_from_dict = GetTransactionList200ResponseTransactionsInnerEntryDetailsTransactionDetails.from_dict(get_transaction_list200_response_transactions_inner_entry_details_transaction_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


