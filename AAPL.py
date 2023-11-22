### Alireza Bahrami (alirzabahrami876@gmail.com)

import yfinance as yf
import pandas as pd

# Grab Data from yfinance
symbol = 'AAPL'
data = yf.download(symbol, start='2022-11-15', end='2023-11-15')

# Add a colum , defualt = Neutral
data['CandleDirection'] = 'Neutral'  # فرض می‌کنیم کندل‌ها ابتدا ناپیوسته هستند

# Fill CandleDirection 
data.loc[data['Close'] > data['Open'], 'CandleDirection'] = 'Up'
data.loc[data['Close'] < data['Open'], 'CandleDirection'] = 'Down'


print(data)
