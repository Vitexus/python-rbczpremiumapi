# CurrencyListSimple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_rate_lists** | [**List[ExchangeRateList]**](ExchangeRateList.md) |  | 

## Example

```python
from rbczpremiumapi.Model.currency_list_simple import CurrencyListSimple

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListSimple from a JSON string
currency_list_simple_instance = CurrencyListSimple.from_json(json)
# print the JSON string representation of the object
print(CurrencyListSimple.to_json())

# convert the object into a dict
currency_list_simple_dict = currency_list_simple_instance.to_dict()
# create an instance of CurrencyListSimple from a dict
currency_list_simple_from_dict = CurrencyListSimple.from_dict(currency_list_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


