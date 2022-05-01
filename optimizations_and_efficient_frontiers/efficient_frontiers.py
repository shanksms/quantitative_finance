from risk_and_returns_fundamentals import edhec_risk_kit
import matplotlib.pyplot as plt
import numpy as np

def portfolio_return(weights, returns):
    return np.dot(weights.T, returns)


def portfolio_volatility(weights, covmat):
    return np.dot(np.dot(weights.T, covmat), weights) ** 0.5

if __name__ == '__main__':
    ind = edhec_risk_kit.get_ind_returns()
    edhec_risk_kit.drawdown(ind['Food'])['draw_down'].plot.line()
    #plt.show()
    annualized_return_1995_to_2000 = edhec_risk_kit.annualized_return(ind['1996':'2000'])
    annualized_return_1995_to_2000.sort_values().plot.bar()
    #plt.show()
    # calculate volatility
    cov = ind['1996': '2000'].cov()
    #print(cov.head())
    weights = np.repeat(1/4, 4)
    l = ['Food', 'Beer', 'Smoke', 'Coal']
    print(portfolio_return(weights, annualized_return_1995_to_2000.loc[l]))
    print(portfolio_volatility(weights, cov.loc[l, l]))

