from risk_and_returns_fundamentals import edhec_risk_kit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from risk_and_returns_fundamentals.edhec_risk_kit import portfolio_return, portfolio_volatility


def port_return_and_vol_demo():
    ind = edhec_risk_kit.get_ind_returns()
    edhec_risk_kit.drawdown(ind['Food'])['draw_down'].plot.line()
    # plt.show()
    annualized_return_1995_to_2000 = edhec_risk_kit.annualized_return(ind['1996':'2000'])
    annualized_return_1995_to_2000.sort_values().plot.bar()
    # plt.show()
    # calculate volatility
    cov = ind['1996': '2000'].cov()
    # print(cov.head())
    weights = np.repeat(1 / 4, 4)
    l = ['Food', 'Beer', 'Smoke', 'Coal']
    print(portfolio_return(weights, annualized_return_1995_to_2000.loc[l]))
    print(portfolio_volatility(weights, cov.loc[l, l]))

def two_asset_efficient_portfolio_demo():
    weight_vec_list = [np.array([w, 1-w]) for w in np.linspace(0, 1, 20)]
    l = ['Games', 'Fin']
    ind = edhec_risk_kit.get_ind_returns()
    annualized_return_1995_to_2000 = edhec_risk_kit.annualized_return(ind['1996':'2000'])
    # plt.show()
    # calculate volatility
    cov = ind['1996': '2000'].cov()
    df = pd.DataFrame(
        {
            'returns': [edhec_risk_kit.portfolio_return(wt_vec, annualized_return_1995_to_2000[l]) for wt_vec in weight_vec_list],
            'volatility': [edhec_risk_kit.portfolio_volatility(wt_vec, cov.loc[l, l]) for wt_vec in weight_vec_list ]
        }
    )
    df.plot.scatter(x='volatility', y='returns')
    plt.show()


if __name__ == '__main__':
    two_asset_efficient_portfolio_demo()

