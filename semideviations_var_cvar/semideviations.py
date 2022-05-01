from risk_and_returns_fundamentals import edhec_risk_kit


hfi = edhec_risk_kit.get_hfi_returns()
print('#' * 80)
print(edhec_risk_kit.semideviation(hfi))
