# ImportPayments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_file_id** | **int** | ID of created batch file | [optional] 

## Example

```python
from rbczpremiumapi.Model.import_payments200_response import ImportPayments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPayments200Response from a JSON string
import_payments200_response_instance = ImportPayments200Response.from_json(json)
# print the JSON string representation of the object
print(ImportPayments200Response.to_json())

# convert the object into a dict
import_payments200_response_dict = import_payments200_response_instance.to_dict()
# create an instance of ImportPayments200Response from a dict
import_payments200_response_from_dict = ImportPayments200Response.from_dict(import_payments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


