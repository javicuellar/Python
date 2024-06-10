import os
from datetime import datetime
import pandas_datareader.data as web

#  uso de datos de Alpha Vantage
#  Usamos el API KEY obtenido de https://www.alphavantage.co/support/#api-key  (correo ralleuc)
apiKey = '30XPO33HBBB0GUFN'
df = web.DataReader("AAPL", "av-daily", start=datetime(2017, 2, 9), end=datetime(2017, 5, 24),
                    api_key=apiKey)

print(df.head(12))
print(df.loc["2017-02-09"])
