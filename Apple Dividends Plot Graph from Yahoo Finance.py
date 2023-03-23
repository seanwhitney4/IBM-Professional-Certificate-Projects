#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install yfinance==0.2.4')
get_ipython().system('pip install pandas==1.3.3')


# In[16]:


import yfinance as yf
import pandas as pd


# In[17]:


apple = yf.Ticker("AAPL")
#create an object that will allow us to access functions to extract data


# In[18]:


get_ipython().system('python -m wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json')


# In[20]:


import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info


# In[11]:


apple_share_price_data = apple.history(period="max")


# In[19]:


apple_share_price_data.head()


# In[21]:


apple.dividends


# In[22]:


apple.dividends.plot()


# In[ ]:




