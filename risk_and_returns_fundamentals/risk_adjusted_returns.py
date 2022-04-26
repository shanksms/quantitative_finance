import pandas as pd
import numpy as np

def compute_volatility_method1(returns_df):
    return returns_df.std()


def compute_volatility_method2(returns_df):
    deviations = returns_df - returns_df.mean()
    squared_deviations = deviations ** 2
    number_of_obs = returns_df.shape[0]
    variance = squared_deviations.sum() / (number_of_obs - 1)
    volatility = variance ** 0.5
    return volatility


def compute_returns(prices_df):
    return prices_df.pct_change()


if __name__ == '__main__':
    sample_prices = pd.read_csv('../data/sample_prices.csv')
    returns_df = compute_returns(sample_prices)
    returns_df = returns_df.dropna()
    volatility = compute_volatility_method1(returns_df)
    volatility2 = compute_volatility_method2(returns_df)
    assert volatility.equals(volatility2)
    """
    Above is monthly volatility.
    we get annualized volatility by multiplying it by sqrt(12) 
    """
    annualized_volatility = np.sqrt(volatility)