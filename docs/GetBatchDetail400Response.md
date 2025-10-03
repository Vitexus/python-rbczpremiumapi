# GetBatchDetail400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Invalid input. | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_batch_detail400_response import GetBatchDetail400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchDetail400Response from a JSON string
get_batch_detail400_response_instance = GetBatchDetail400Response.from_json(json)
# print the JSON string representation of the object
print(GetBatchDetail400Response.to_json())

# convert the object into a dict
get_batch_detail400_response_dict = get_batch_detail400_response_instance.to_dict()
# create an instance of GetBatchDetail400Response from a dict
get_batch_detail400_response_from_dict = GetBatchDetail400Response.from_dict(get_batch_detail400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


