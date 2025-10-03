# GetBalance429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_balance429_response import GetBalance429Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalance429Response from a JSON string
get_balance429_response_instance = GetBalance429Response.from_json(json)
# print the JSON string representation of the object
print(GetBalance429Response.to_json())

# convert the object into a dict
get_balance429_response_dict = get_balance429_response_instance.to_dict()
# create an instance of GetBalance429Response from a dict
get_balance429_response_from_dict = GetBalance429Response.from_dict(get_balance429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


