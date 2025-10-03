# DownloadStatementRequest

Request values for the statement download.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Number of the account without prefix and bank code. | 
**currency** | **str** | Currency of the requested currency folder. | [optional] 
**statement_id** | **str** | Public id of the statement. | 
**statement_format** | **str** | The format of the statement. | 

## Example

```python
from rbczpremiumapi.Model.download_statement_request import DownloadStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadStatementRequest from a JSON string
download_statement_request_instance = DownloadStatementRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadStatementRequest.to_json())

# convert the object into a dict
download_statement_request_dict = download_statement_request_instance.to_dict()
# create an instance of DownloadStatementRequest from a dict
download_statement_request_from_dict = DownloadStatementRequest.from_dict(download_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


