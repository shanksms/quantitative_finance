import pandas as pd

file_path = r'../data/Portfolios_Formed_on_ME_monthly_EW.csv'

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

if __name__ == '__main__':
    print(get_ffme_returns().head())
    print(get_ffme_returns().head())