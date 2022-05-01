from risk_and_returns_fundamentals import edhec_risk_kit
import pandas as pd
from scipy.stats import skew
import numpy as np

hfi = edhec_risk_kit.get_hfi_returns()
df = pd.concat([hfi.mean(), hfi.median(), hfi.mean() > hfi.median()], axis=1)
print(hfi.head())
print('#' * 80)
print('skewness using custom code')
print(edhec_risk_kit.skewness(hfi).sort_values())

print('#' * 80)
print('skewness using scipy code')
print(skew(hfi))
print('#' * 80)
print('skewness of normal returns')
normal_rets = np.random.normal(0, 0.15, size=(26300, 1))
#print(normal_rets)
print(edhec_risk_kit.skewness(normal_rets))

print('#' * 80)
print('using jarque-bera test on normal returns')
print(edhec_risk_kit.is_normal(normal_rets))
print('#' * 80)
print('using jarque-bera test on hfi returns')
print(hfi.aggregate(edhec_risk_kit.is_normal))

