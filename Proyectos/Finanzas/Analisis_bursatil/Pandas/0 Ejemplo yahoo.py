import pandas_datareader.data as web
import pandas as pd
import datetime as dt

# yahoo - retrieve daily stock prices (high, open, close, volu,e and adjusted close)
# yahoo-actions - retrieve historical corporate actions (dividends and stock splits)
# yahoo-dividends - retrieve historical dividends
df = web.DataReader('GOOG', 'yahoo', start='2019-09-10', end='2019-10-09')
print("Precios Google\n", df.head())


inicio = dt.datetime(2010, 1, 29)
fin = dt.datetime.today()
actions = web.DataReader('GOOG', 'yahoo-actions', inicio, fin)
print("\nSsplits: \n", actions.head())


dividendos = web.DataReader('IBM', 'yahoo-dividends', inicio, fin)
print("\nDividendos: \n", dividendos.head())

