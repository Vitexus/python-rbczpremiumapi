# ExchangeRateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date_from** | **datetime** |  | 
**effective_date_to** | **datetime** |  | [optional] 
**trading_date** | **datetime** |  | 
**ordinal_number** | **int** |  | 
**last_rates** | **bool** |  | 
**exchange_rates** | [**List[ExchangeRate]**](ExchangeRate.md) |  | 

## Example

```python
from rbczpremiumapi.Model.exchange_rate_list import ExchangeRateList

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateList from a JSON string
exchange_rate_list_instance = ExchangeRateList.from_json(json)
# print the JSON string representation of the object
print(ExchangeRateList.to_json())

# convert the object into a dict
exchange_rate_list_dict = exchange_rate_list_instance.to_dict()
# create an instance of ExchangeRateList from a dict
exchange_rate_list_from_dict = ExchangeRateList.from_dict(exchange_rate_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


