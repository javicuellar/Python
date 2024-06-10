#  Sacado de https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/

import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt


Tesla = data.DataReader("TSLA", "yahoo", start="2022-1-1")
print(Tesla.info())

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2022-01-01'
end_date = '2022-09-19'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(tickers, "yahoo", start_date, end_date)
print(panel_data.head(9))

# Nos quedamos sólo con los precios de cierre "Close"
close = panel_data['Close']

# Obtenemos todos los días de la semana entre 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# Rehacemos el dataframe de cierre con todos los días de la semana
close = close.reindex(all_weekdays)

# Reindexar el dataframe ha hecho que las fechas de fin de semana añadidas no tengan
# datos (NaN), para estos valores rellenamos con el último valor disponible del ticket.
close = close.fillna(method='ffill')

# Revisamos el dataframe obtenido
print(close.describe())

# Get the MSFT timeseries. This now returns a Pandas Series object indexed by date.
msft = close.loc[:, 'MSFT']

# Calculate the 20 and 100 days moving averages of the closing prices
short_rolling_msft = msft.rolling(window=20).mean()
long_rolling_msft = msft.rolling(window=100).mean()

# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(msft.index, msft, label='MSFT')
ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()

plt.show()