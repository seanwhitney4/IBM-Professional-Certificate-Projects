#!/usr/bin/env python
# coding: utf-8

# In[38]:


#This exercise focused on importing panadas to learn how to create and analyze a DataFrame. 
#(Part of IBM Data Analytics Professional Certificate)


# In[ ]:





# In[18]:


import pandas as pd
a = {'Player':['Kevin Durant', 'Steph Curry', 'Ja Morant', 'Devin Booker'],
     'Age':['27', '24', '22', '32'],
     'City':['Phoenix', 'Golden State', 'Memphis', 'Phoenix'],
     'Team':['Suns','Warriors','Grizzlies','Suns'],
     'Career Points':['26764','21183','5397','12450']}
df = pd.DataFrame(a)
df


# In[12]:


b= df [['Player']]
b


# In[11]:


c = df [['City','Team']]
c


# In[14]:


d = df ['Career Points']
d


# In[19]:


type(df)


# In[21]:


df.loc[0,'Career Points']
#Locating the highest Career PPG in df


# In[35]:


df.loc['Ja Morant','Career Points']
#Locating specific information by row and column


# In[42]:


df.iloc[0:5, 1:3]
#Using Slices to only include player and team information


# In[44]:


df.loc['Kevin Durant':'Devin Booker','City':'Team']
#Another way to slice to data without counting rows and columns


# In[ ]:




