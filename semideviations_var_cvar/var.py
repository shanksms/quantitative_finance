import numpy as np
import pandas as pd
from risk_and_returns_fundamentals import edhec_risk_kit

hfi = edhec_risk_kit.get_hfi_returns()
# Calculate var at 5%

#There is a 5% chance that, in any month you are going to lose var_5ct or worse
print('#' * 80)
print('Historic VaR')
print(edhec_risk_kit.var_historic(hfi, level=5))
print('#' * 80)
print('Gaussian VaR')
print(edhec_risk_kit.var_gaussian(hfi, level=5))
print('#' * 80)
print('Cornish-Fischer VaR')
print(edhec_risk_kit.var_gaussian(hfi, level=5, modified=True))
print('#' * 80)
print('conditional VaR')

