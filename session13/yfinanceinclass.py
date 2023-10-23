# in command prompt: "python -mpip install yfinance"

import yfinance as yf
import pprint

tsla = yf.Ticker('TSLA') #a Ticker insance (OOP)

print(tsla.info)