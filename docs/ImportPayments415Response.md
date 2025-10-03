# ImportPayments415Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.import_payments415_response import ImportPayments415Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPayments415Response from a JSON string
import_payments415_response_instance = ImportPayments415Response.from_json(json)
# print the JSON string representation of the object
print(ImportPayments415Response.to_json())

# convert the object into a dict
import_payments415_response_dict = import_payments415_response_instance.to_dict()
# create an instance of ImportPayments415Response from a dict
import_payments415_response_from_dict = ImportPayments415Response.from_dict(import_payments415_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


