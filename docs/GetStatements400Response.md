# GetStatements400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Invalid date. | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_statements400_response import GetStatements400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatements400Response from a JSON string
get_statements400_response_instance = GetStatements400Response.from_json(json)
# print the JSON string representation of the object
print(GetStatements400Response.to_json())

# convert the object into a dict
get_statements400_response_dict = get_statements400_response_instance.to_dict()
# create an instance of GetStatements400Response from a dict
get_statements400_response_from_dict = GetStatements400Response.from_dict(get_statements400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


