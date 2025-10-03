# GetStatements200ResponseStatementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | public id of the statement | 
**account_id** | **int** | account id | 
**statement_number** | **str** | number of the statement | 
**date_from** | **date** | valid date from for statement | 
**date_to** | **date** | valid date to for statement | 
**currency** | **str** | currency of the statement | [optional] 
**statement_formats** | **List[str]** | set of document available formats (always in upper case notation). | 

## Example

```python
from rbczpremiumapi.Model.get_statements200_response_statements_inner import GetStatements200ResponseStatementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatements200ResponseStatementsInner from a JSON string
get_statements200_response_statements_inner_instance = GetStatements200ResponseStatementsInner.from_json(json)
# print the JSON string representation of the object
print(GetStatements200ResponseStatementsInner.to_json())

# convert the object into a dict
get_statements200_response_statements_inner_dict = get_statements200_response_statements_inner_instance.to_dict()
# create an instance of GetStatements200ResponseStatementsInner from a dict
get_statements200_response_statements_inner_from_dict = GetStatements200ResponseStatementsInner.from_dict(get_statements200_response_statements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


