# ImportPayments400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | * INVALID_BATCH_IMPORT_FORMAT - Batch-Import-Format unsupported * BATCH_CONTENT_INVALID - Batch content doesn&#39;t match to declared Batch-Import-Format * BATCH_ALREADY_IMPORTED - Batch has already been imported (based on checksum)  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.import_payments400_response import ImportPayments400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPayments400Response from a JSON string
import_payments400_response_instance = ImportPayments400Response.from_json(json)
# print the JSON string representation of the object
print(ImportPayments400Response.to_json())

# convert the object into a dict
import_payments400_response_dict = import_payments400_response_instance.to_dict()
# create an instance of ImportPayments400Response from a dict
import_payments400_response_from_dict = ImportPayments400Response.from_dict(import_payments400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


