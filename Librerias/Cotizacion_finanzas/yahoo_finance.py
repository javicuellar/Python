import pandas
import numpy
# instalacion:  pip install ta-lib   (necesita Microsoft Visual C++ 14.0 o superior)
# import talib

import matplotlib.pyplot as plt

 # No funciona, desinstalo la librería
from yahoo_finance import Share

s = Share('BIMBOA.MX')

historical = s.get_historical('2014-10-24','2015-10-24')

class Lamb(object):
    high  = []
    low	  = []
    close = []

    def __init__(self, high, low, close):
        self.high
        self.low
        self.close
    

def parseYahooHistorical(historical):
    high  = []
    low	  = []
    close = []

    for day in historical:
        high.append(float(day['High']))
        low.append(float(day['Low']))
        close.append(float(day['Close']))

    return Lamb(high, low, close)

#lamb = parseYahooHistorical(h)

close = []
for day in historical:
	close.append(float(day['Close']))

close = numpy.array(pandas.Series(close))

#print close

macd = talib.MACD(close)
s_dev = talib.STDDEV(close, startIdx=0, endIdx=100)
print (s_dev)

#plt.plot(macd[0])
#plt.show()