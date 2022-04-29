from risk_and_returns_fundamentals import edhec_risk_kit
import pandas as pd

hfi = edhec_risk_kit.get_hfi_returns()
df = pd.concat([hfi.mean(), hfi.median(), hfi.mean() > hfi.median()], axis=1)
print(df.head())


