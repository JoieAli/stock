import pandas as pd
import pandas_datareader as pdr
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# start = datetime(2018, 5, 1)
# alibaba = pdr.get_data_yahoo("BABA", start=start)
# alibaba.to_csv("/home/joiejiang/PycharmProjects/stock/alibaba")
# alibaba['Adj Close'].plot(kind='line', legend=True)
# print(alibaba.head(5))

alibaba = pd.read_csv("/home/joiejiang/PycharmProjects/stock/alibaba")
print(type(alibaba))
closeprice = alibaba['Close']
print(closeprice[0], type(closeprice))


