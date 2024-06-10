#  Sacado de https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/

import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt
import statsmodels.formula.api as smf


#  Seleccionamos los activos: Apple, Microsoft y indice S&P500.
tickers = ['AAPL', 'MSFT', '^GSPC']
start_date = '2022-01-01'
end_date = dt.date.today()

panel_data = data.DataReader(tickers, "yahoo", start_date, end_date)

close = panel_data['Close']     # Nos quedamos con los precios de cierre

#    Seleccionamos los datos de Microsoft, devuelve un pandas series indexado por fecha
activo = 'AAPL'
analisis = close.loc[:, activo]

#  Calculamos medias de 10, 20 y 50 días
s_rolling = analisis.rolling(window=10).mean()
short_rolling = analisis.rolling(window=20).mean()
long_rolling = analisis.rolling(window=50).mean()

#  Representamos el activo y sus medias 10, 20 y 50 días
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(analisis.index, analisis, label=activo)
ax.plot(s_rolling.index, s_rolling, label='10 days rolling')
ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
ax.plot(long_rolling.index, long_rolling, label='50 days rolling')
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.show()


#  Calculamos la Recta de Regresión Lineal y la tabla ANOVA 
x = analisis
y = analisis.index

rls = smf.ols(formula="y~x", data=df).fit()
parametros = rlsEntrenado.params
print(parametros)
print(f"Ecuación Y = {parametros.Intercept:.4} {parametros.x:.3} * x")

xn = sm.add_constant(analisis.index)         # añadimos columna constante
modeloAnova = sm.OLS(analisis, xn).fit()
print("\nTabla ANOVA")
print(modeloAnova.summary())