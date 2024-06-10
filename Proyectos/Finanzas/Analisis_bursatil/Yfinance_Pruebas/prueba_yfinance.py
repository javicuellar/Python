import yfinance as yf

#   Descargar el historial de Apple (AAPL) desde el 1 enero 2024 al 8 de marzo 2024
# aapl = yf.download('AAPL', start='2024-01-01', end='2024-03-09')
nvidia1 = yf.download('NVDA')

#   Imprimimos los primeros registros del dataframe
print(nvidia1)


nvidia2 = yf.Ticker("NVDA")
print(nvidia2)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
# nvidia2.info
''' Devuelve error HTTPError: 401 Unauthorized'''

# get historical market data
print(nvidia2.history(period="max"))

# show actions (dividends, splits)
print('-------------\n', nvidia2.actions)

# show dividends
print('-------------\n', nvidia2.dividends)

# show splits
print('-------------\n', nvidia2.splits)
