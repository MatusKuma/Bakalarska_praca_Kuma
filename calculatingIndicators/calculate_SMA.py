import pandas as pd
from ta.trend import SMAIndicator


file = pd.read_csv('../data/BTCUSD_1h_with_indicators.csv')

sma_7 = SMAIndicator(file['close'], window=7)
file['SMA_7'] = sma_7.sma_indicator()
file.to_csv('BTCUSD_1h_with_indicators.csv', index = False)


sma_20 = SMAIndicator(file['close'], window=20)
file['SMA_20'] = sma_20.sma_indicator()
file.to_csv('BTCUSD_1h_with_indicators.csv', index = False)
