#STOCK PRICES ARE REALLY HARD TO PREDICT AN THE ANAYLISIS OF THEIR ACF AND PACF SUPPORT THAT 

#source: https://github.com/ritvikmath/Time-Series-Analysis/blob/master/Time%20Series%20Data.ipynb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()

import yfinance as yf

#define the ticker symbol
tickerSymbol = 'SPY'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)


#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-1-1', end='2020-1-1')

tickerDf = tickerDf[['Close']]


#see your data
print(tickerDf.head())


#Plot s&p data (2015-2021)
plt.figure(figsize=(10,4))
plt.plot(tickerDf.Close)
plt.title('Stock Price over Time (%s)'%tickerSymbol, fontsize=20)
plt.ylabel('Price', fontsize=16)
for year in range(2015,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
#plt.show()



#Stationarity: take first difference of this series

#take first difference
first_diffs = tickerDf.Close.values[1:] - tickerDf.Close.values[:-1]
first_diffs = np.concatenate([first_diffs, [0]])

#set first difference as variable in dataframe
tickerDf['FirstDifference'] = first_diffs


print(tickerDf.head())


plt.figure(figsize=(10,4))
plt.plot(tickerDf.FirstDifference)
plt.title('First Difference over Time (%s)'%tickerSymbol, fontsize=20)
plt.ylabel('Price Difference', fontsize=16)
for year in range(2015,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)

#plt.show()


#ACF isn't that informative
acf_plot = plot_acf(tickerDf.FirstDifference)



#PACF also doesn't tell us much

pacf_plot = plot_pacf(tickerDf.FirstDifference)
plt.show()
