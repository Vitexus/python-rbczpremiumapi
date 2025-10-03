# ImportPayments413Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.import_payments413_response import ImportPayments413Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPayments413Response from a JSON string
import_payments413_response_instance = ImportPayments413Response.from_json(json)
# print the JSON string representation of the object
print(ImportPayments413Response.to_json())

# convert the object into a dict
import_payments413_response_dict = import_payments413_response_instance.to_dict()
# create an instance of ImportPayments413Response from a dict
import_payments413_response_from_dict = ImportPayments413Response.from_dict(import_payments413_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


