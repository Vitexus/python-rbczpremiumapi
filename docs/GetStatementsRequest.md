# GetStatementsRequest

Request values for list of a statements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**currency** | **str** | Currency of the requested currency folder. | [optional] 
**statement_line** | **str** | Statement line identification. | [optional] 
**date_from** | **date** | Date limit from. | [optional] 
**date_to** | **date** | Date limit to. | [optional] 

## Example

```python
from rbczpremiumapi.Model.get_statements_request import GetStatementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatementsRequest from a JSON string
get_statements_request_instance = GetStatementsRequest.from_json(json)
# print the JSON string representation of the object
print(GetStatementsRequest.to_json())

# convert the object into a dict
get_statements_request_dict = get_statements_request_instance.to_dict()
# create an instance of GetStatementsRequest from a dict
get_statements_request_from_dict = GetStatementsRequest.from_dict(get_statements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


