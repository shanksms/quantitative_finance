import pandas as pd
from scipy import stats
import numpy as np
from scipy.stats import norm

file_path = r'../data/Portfolios_Formed_on_ME_monthly_EW.csv'


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


def drawdown(return_series):
    """
        1. Compute Wealth index
        2. Compute previous peaks
        3. Compute draw down which is the wealth value as a percentage of previous peaks
        :return:
        """
    starting_capital = 1000
    wealth_index = starting_capital * ((1 + return_series).cumprod())
    previous_peaks = wealth_index.cummax()
    draw_down = (wealth_index - previous_peaks) / previous_peaks
    return pd.DataFrame(
        {
            'wealth_index': wealth_index,
            'previous_peaks': previous_peaks,
            'draw_down': draw_down
        }
    )

def get_ffme_returns():
    portfolio_returns_df = pd.read_csv(file_path,
                                       header=0, index_col=0, na_values=-99.99, parse_dates=True).loc[:,
                           ['Lo 10', 'Hi 10']]
    portfolio_returns_df.rename(columns={'Lo 10': 'SmallCap', 'Hi 10': 'LargeCap'}, inplace=True)
    portfolio_returns_df.index = pd.to_datetime(portfolio_returns_df.index, format='%Y%m')
    portfolio_returns_df.index = portfolio_returns_df.index.to_period('M')
    return portfolio_returns_df / 100

def get_hfi_returns():
    hfi = pd.read_csv('../data/edhec-hedgefundindices.csv', header=0, index_col=0, parse_dates=True)
    hfi = hfi/100
    hfi.index = hfi.index.to_period('M')
    return hfi


def skewness(returns):
    return skewness_kurtosis(returns, 3)


def kurtosis(returns):
    return skewness_kurtosis(returns, 4)


def skewness_kurtosis(returns, power):
    std = returns.std(ddof=0)
    demeaned_returns = returns - returns.mean()
    return (demeaned_returns ** power).mean() / std ** power


def is_normal(r, level=0.1):
    """
    Applies JArque-bera test to determine if a series is normal or not.
    Test is applied at the level 1% by default.
    :param r:
    :param level:
    :return:
    """
    statistics, pvalue = stats.jarque_bera(r)
    return pvalue > level


def semideviation(returns):
    return returns[returns < 0].std(ddof=0)


def var_historic(r, level=5):
    """
    var historic
    :param r:
    :param level:
    :return:
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError('expected to be series or Datafram')

def var_gaussian(r: pd.DataFrame, level=5, modified=False):
    """
    returns the parametric gaussian VaR of a series or Dataframe
    :param r:
    :param level:
    :return:
    """
    # Compute z score assuming it was Gaussian distribution
    z = norm.ppf(level/100) # Find the z-score of .5 percent line of a Gaussian distribution
    # Below should return 0
    #print(norm.ppf(0.5))
    if modified:
        # calculate Cornish Fischer VaR
        s = skewness(r)
        k = kurtosis(r)
        z = (z +
             (z**2 -1)*s/6 +
             (z**3 -3*z)*(k-3)/24 -
             (2*z**3 -5*z)*(s**2)/36
        )

    return -(r.mean() + z * r.std(ddof=0))


def get_ind_returns():
    ind = pd.read_csv('../data/ind30_m_vw_rets.csv', header=0, index_col=0)/100
    ind.index = pd.to_datetime(ind.index, format='%Y%m').to_period('M')
    ind.columns = ind.columns.str.strip()
    return ind


def portfolio_return(weights, returns):
    return np.dot(weights.T, returns)


def portfolio_volatility(weights, covmat):
    return np.dot(np.dot(weights.T, covmat), weights) ** 0.5

if __name__ == '__main__':
    print(get_ffme_returns().head())
    print(get_ffme_returns().head())
    print(get_ind_returns().head())