import pandas as pd
import pandas_datareader as pdr
alibaba = pdr.get_data_yahoo("BABA")
print(alibaba.head(5))
print(alibaba.size)
print(alibaba.shape)
print(alibaba.info)
