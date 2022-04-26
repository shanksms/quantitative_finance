import pandas as pd
import matplotlib.pyplot as plt

file_path = r'../data/Portfolios_Formed_on_ME_monthly_EW.csv'

def read_returns():
    portfolio_returns_df = pd.read_csv(file_path,
                                       header=0, index_col=0, na_values=-99.99, parse_dates=True).loc[:,
                           ['Lo 10', 'Hi 10']]
    portfolio_returns_df.rename(columns={'Lo 10': 'SmallCap', 'Hi 10': 'LargeCap'}, inplace=True)
    portfolio_returns_df.index = pd.to_datetime(portfolio_returns_df.index, format='%Y%m')
    portfolio_returns_df.index = portfolio_returns_df.index.to_period('M')
    return portfolio_returns_df / 100

def compute_draw_down(portfolio_returns_df, starting_capital=1000, LargeCap='LargeCap'):
    """
    1. Compute Wealth index
    2. Compute previous peaks
    3. Compute draw down which is the wealth value as a percentage of previous peaks
    :return:
    """

    wealth_index = starting_capital * ((1 + portfolio_returns_df[LargeCap]).cumprod())
    previous_peaks = wealth_index.cummax()
    draw_down = (wealth_index - previous_peaks) / previous_peaks
    return pd.DataFrame(
        {
            'wealth_index': wealth_index,
            'previous_peaks': previous_peaks,
            'draw_down': draw_down
        }
    )

if __name__ == '__main__':
    rets = read_returns()
    draw_down = compute_draw_down(rets)
    print(draw_down.head())
    draw_down.loc[:, ['wealth_index', 'previous_peaks']].plot.line()
    plt.show()
    draw_down.loc[:, 'draw_down'].plot.line()
    plt.show()

    """
    max drawdown since 1975
    """
    max_drawdown_since1975 = draw_down.loc[:, 'draw_down'].loc['1975':].min()
    print('#' * 80)
    print('maximum drawdown since 1975')
    print(max_drawdown_since1975)
    """
    find out when max drawdown since 1975 happened
    """
    period = draw_down.loc[:, 'draw_down'].loc['1975':].idxmin()
    print('#' * 80)
    print('when maximum drawdown since 1975 happened')
    print(period)
