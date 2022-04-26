import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'../data/Portfolios_Formed_on_ME_monthly_EW.csv'
risk_free_rate = 0.03


def read_returns():
    portfolio_returns_df = pd.read_csv(file_path,
                                       header=0, index_col=0, na_values=-99.99, parse_dates=True).loc[:,
                           ['Lo 10', 'Hi 10']]
    portfolio_returns_df.rename(columns={'Lo 10': 'SmallCap', 'Hi 10': 'LargeCap'}, inplace=True)
    """
    returns are mentioned in percentages. Divide them by 100
    
    """
    return portfolio_returns_df / 100


def annualized_vol(return_df):
    return return_df.std()*np.sqrt(12)

def annualized_return(return_df):
    """

    :param return_df:
    :return:
    """
    number_of_months = return_df.shape[0]
    total_return = (1 + return_df).prod() - 1
    monthly_return = (1 + return_df).prod()**(1/number_of_months) - 1
    annual_return = (1+monthly_return)**12 - 1
    """
    short form is below:
    (1 + return_df).prod()**(12/number_of_months) - 1
    """
    return annual_return


def sharpe_ratio(annualized_returns, annualized_vol):
    # Higher sharpe ratio is better
    return (annualized_returns - risk_free_rate) / annualized_vol


if __name__ == '__main__':
    return_df = read_returns()
    print(return_df.head())
    return_df.plot.line()
    plt.show()
    print('#' * 80)
    print('annualized volatility')
    print(annualized_vol(return_df))
    print('#' * 80)
    print('annualized return')
    print(annualized_return(return_df))
    print('#' * 80)
    print('sharpe ratio')
    print(
        sharpe_ratio(annualized_return(return_df), annualized_vol(return_df))
    )
