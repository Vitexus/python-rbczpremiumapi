# GetBatchDetail200ResponseBatchItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_info** | [**GetBatchDetail200ResponseBatchItemsInnerAccountInfo**](GetBatchDetail200ResponseBatchItemsInnerAccountInfo.md) |  | [optional] 
**number_of_payments** | **int** | Number of payments within the batch | [optional] 
**sum_amount** | **float** | Sum amount | [optional] 
**sum_amount_currency_id** | **str** | The currency folder identification (CATALOG: CURRENCIES) | [optional] 
**batch_type** | **str** | Batch transaction package payment type | [optional] 
**status** | **str** | Bacth transaction package status | [optional] 
**assigned_user_name** | **str** | Name of user assigned to batch transaction package | [optional] 
**last_change_date_time** | **datetime** | Date and time of last change of batch transaction package | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_batch_detail200_response_batch_items_inner import GetBatchDetail200ResponseBatchItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchDetail200ResponseBatchItemsInner from a JSON string
get_batch_detail200_response_batch_items_inner_instance = GetBatchDetail200ResponseBatchItemsInner.from_json(json)
# print the JSON string representation of the object
print(GetBatchDetail200ResponseBatchItemsInner.to_json())

# convert the object into a dict
get_batch_detail200_response_batch_items_inner_dict = get_batch_detail200_response_batch_items_inner_instance.to_dict()
# create an instance of GetBatchDetail200ResponseBatchItemsInner from a dict
get_batch_detail200_response_batch_items_inner_from_dict = GetBatchDetail200ResponseBatchItemsInner.from_dict(get_batch_detail200_response_batch_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


