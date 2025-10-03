# GetStatements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | [**List[GetStatements200ResponseStatementsInner]**](GetStatements200ResponseStatementsInner.md) | An array of statements. | 
**page** | **int** | Page number. | 
**size** | **int** | Page size. | 
**first** | **bool** | Is this the first page? | 
**last** | **bool** | Is this the last page? | 
**total_pages** | **int** | Total number of pages. | 
**total_size** | **int** | Total number of items. | 

## Example

```python
from rbczpremiumapi.Model.get_statements200_response import GetStatements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatements200Response from a JSON string
get_statements200_response_instance = GetStatements200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatements200Response.to_json())

# convert the object into a dict
get_statements200_response_dict = get_statements200_response_instance.to_dict()
# create an instance of GetStatements200Response from a dict
get_statements200_response_from_dict = GetStatements200Response.from_dict(get_statements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


