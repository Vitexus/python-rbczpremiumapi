# GetBatchDetail200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_name** | **str** | Batch name | [optional] 
**batch_file_status** | **str** | Status of batch file import | [optional] 
**create_date** | **date** | The date when the batch was created | [optional] 
**batch_items** | [**List[GetBatchDetail200ResponseBatchItemsInner]**](GetBatchDetail200ResponseBatchItemsInner.md) |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_batch_detail200_response import GetBatchDetail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchDetail200Response from a JSON string
get_batch_detail200_response_instance = GetBatchDetail200Response.from_json(json)
# print the JSON string representation of the object
print(GetBatchDetail200Response.to_json())

# convert the object into a dict
get_batch_detail200_response_dict = get_batch_detail200_response_instance.to_dict()
# create an instance of GetBatchDetail200Response from a dict
get_batch_detail200_response_from_dict = GetBatchDetail200Response.from_dict(get_batch_detail200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


