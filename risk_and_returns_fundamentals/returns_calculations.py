import pandas as pd
import matplotlib.pyplot as plt

prices = pd.read_csv('../data/sample_prices.csv')
# Both returns 1 and returns 2 should be same
returns = prices.pct_change()
returns2 = prices/prices.shift(1) - 1
assert returns.shape[0] == returns2.shape[0]
print(returns)
print('#' * 80)
print(returns2)

prices.plot()
returns.plot.bar()
plt.show()
print('#' * 80)
print('std')
print(returns.std())
# Lets find out compounded return
"""
recall that if rate of change is, then over n time period, compounded returns will be (1+r)^n - 1
if rete of change is r1, r2, ...rn, then compounded return will be (1+r1)(1+r2)....(1+rn) - 1
"""
print('#' * 80)
print('compounded return')
compounded_return = (1 + returns).prod() - 1
print(compounded_return)



