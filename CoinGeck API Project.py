#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using CoinGecko API to create a candlestick chart for BTC based on the min, max, open and close prices of the day


# In[5]:


get_ipython().system('pip install pycoingecko')
get_ipython().system('pip install plotly')
get_ipython().system('pip install mplfinance')
get_ipython().system('pip install --upgrade nbformat')


# In[6]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


# In[11]:


cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)


# In[12]:


bitcoin_price_data = bitcoin_data['prices']

bitcoin_price_data[0:5]


# In[14]:


data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
#Turning this into a Pandas DataFrame


# In[15]:


data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
#Now that we have the DataFrame I converted the timestamp to datetime and saved it as a column called Date. 


# In[16]:


candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})


# In[17]:


fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()


# In[ ]:




