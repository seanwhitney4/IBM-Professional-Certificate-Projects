#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This project was to perform basic exploratory data analysis using SQL and python visualization tools including matplotlib


# In[ ]:


# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql


# In[ ]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[ ]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://')


# In[ ]:


import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
get_ipython().run_line_magic('sql', 'PERSIST chicago_socioeconomic_data')


# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data;')
#To get the amount of rows in the data set


# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;')
#How many community areas in Chicago have a hardship index greater than 50.0?


# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;')
#Which Chicago community areas have per-capita incomes greater than $60,000?


# In[ ]:


#Create a scatter plot using the variables per_capita_income_ and hardship_index
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# In[ ]:




