# ExchangeRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_flag_path** | **str** |  | [optional] 
**currency_from** | **str** |  | 
**currency_to** | **str** |  | 
**exchange_rate_buy** | **float** |  | 
**exchange_rate_buy_cash** | **float** |  | 
**exchange_rate_center** | **float** |  | 
**exchange_rate_center_change** | **float** |  | 
**exchange_rate_sell** | **float** |  | 
**exchange_rate_sell_cash** | **float** |  | 
**exchange_rate_sell_center** | **float** |  | 
**exchange_rate_sell_center_previous** | **float** |  | 
**exchange_rate_ecb_rate** | **float** |  | [optional] 
**exchange_rate_ecb_variation** | **float** |  | [optional] 
**fixed_country_code** | **str** |  | [optional] 
**fixed_country_name** | **str** |  | [optional] 
**quotation_type** | **str** |  | 
**units_from** | **int** |  | 
**variable_country_code** | **str** |  | [optional] 
**variable_country_name** | **str** |  | [optional] 

## Example

```python
from rbczpremiumapi.Model.exchange_rate import ExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRate from a JSON string
exchange_rate_instance = ExchangeRate.from_json(json)
# print the JSON string representation of the object
print(ExchangeRate.to_json())

# convert the object into a dict
exchange_rate_dict = exchange_rate_instance.to_dict()
# create an instance of ExchangeRate from a dict
exchange_rate_from_dict = ExchangeRate.from_dict(exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


