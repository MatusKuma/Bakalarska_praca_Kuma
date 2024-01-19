import pandas as pd
from ta.momentum import RSIIndicator


file = pd.read_csv('BTCUSD_1h_with_indicators.csv')

rsi = RSIIndicator(file['close'], window=14)
file['RSI'] = rsi.rsi()
file.to_csv('BTCUSD_1h_with_indicators.csv', index = False)
