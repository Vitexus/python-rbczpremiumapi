# GetBalance403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_balance403_response import GetBalance403Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalance403Response from a JSON string
get_balance403_response_instance = GetBalance403Response.from_json(json)
# print the JSON string representation of the object
print(GetBalance403Response.to_json())

# convert the object into a dict
get_balance403_response_dict = get_balance403_response_instance.to_dict()
# create an instance of GetBalance403Response from a dict
get_balance403_response_from_dict = GetBalance403Response.from_dict(get_balance403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


