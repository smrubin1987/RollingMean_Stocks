##Algorithmic Trading in Python: Moving Averages##

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os 

#get todays date
today = date.today()
today = today.strftime("%m-%d-%Y")

directory = r"C:\Users\srubin\OneDrive - INTERA Inc\Untitled Folder"
os.chdir(directory)

#create subdirectory based on the date
if not os.path.exists(today):
    os.makedirs(today)

def grapher():

    #list of asset tickers
    tickers = ['MSFT','AAPL','VOO','J','BXMT','BX','BNS','NIO','EIX', 'VYM',
    'ABBV', 'AZN', 'RIO', 'GOLD','O', 'MAIN','BTC-USD', 'STWD', 'VCIT',
    'TM', 'RTX','MA', 'SACH']
    
    #loop through tickers, get data, and analyze
    for t in tickers:
        print(t)
        ticker = yf.Ticker(t)
        print(ticker)
        v = yf.download(t)
        v = pd.DataFrame(v)
                    
        #Create Moving Averages
        SMA10 = v['Close'].rolling(window = 10).mean()
        SMA20 = v['Close'].rolling(window = 20).mean()
        SMA50 = v['Close'].rolling(window = 50).mean()
        SMA100 = v['Close'].rolling(window = 100).mean()
        
        #obtain max, mean prices
        max_price = v[-200:].Close.max()
        mean_price = ((max_price) + (v[-200:].Close.min()))/2
        
        #taking last 500 trading days and graph
        plt.figure(figsize=(15, 6))
        plt.plot(v['Close'][-500:], label=t, linestyle='--')
        plt.plot(SMA10[-500:], label='SMA10')
        plt.plot(SMA20[-500:], label='SMA20')
        plt.plot(SMA50[-500:], label='SMA50')
        plt.plot(SMA100[-500:], label='SMA100')
        plt.axhline(y=max_price, linestyle='--', label='Max Price Past 200d')
        plt.axhline(y=mean_price, linestyle='--', label = 'Mean Price Past 200d')
        plt.legend(loc='upper left', fontsize=15)
        plt.title(t + ": Moving Averages Analysis")
        plt.grid()
        #plt.show()
        plt.savefig(today + "/"  + t + "_" + "MovingAvgAnalysis_" + today +".png")
        
grapher()
