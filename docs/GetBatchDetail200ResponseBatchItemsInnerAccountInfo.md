# GetBatchDetail200ResponseBatchItemsInnerAccountInfo

Account info detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account Id. | 
**account_number_prefix** | **str** | Charged account number prefix | [optional] 
**account_number** | **str** | Charged account number | 
**main_currency_id** | **str** | The currency folder identification (CATALOG: CURRENCIES) | 

## Example

```python
from rbczpremiumapi.Model.get_batch_detail200_response_batch_items_inner_account_info import GetBatchDetail200ResponseBatchItemsInnerAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchDetail200ResponseBatchItemsInnerAccountInfo from a JSON string
get_batch_detail200_response_batch_items_inner_account_info_instance = GetBatchDetail200ResponseBatchItemsInnerAccountInfo.from_json(json)
# print the JSON string representation of the object
print(GetBatchDetail200ResponseBatchItemsInnerAccountInfo.to_json())

# convert the object into a dict
get_batch_detail200_response_batch_items_inner_account_info_dict = get_batch_detail200_response_batch_items_inner_account_info_instance.to_dict()
# create an instance of GetBatchDetail200ResponseBatchItemsInnerAccountInfo from a dict
get_batch_detail200_response_batch_items_inner_account_info_from_dict = GetBatchDetail200ResponseBatchItemsInnerAccountInfo.from_dict(get_batch_detail200_response_batch_items_inner_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


