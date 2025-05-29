# # GetTransactionList200ResponseTransactionsInner

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

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
