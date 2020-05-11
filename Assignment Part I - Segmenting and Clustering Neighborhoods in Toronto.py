#!/usr/bin/env python
# coding: utf-8

# In[49]:


postalCode_Canada=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")

df=postalCode_Canada[0]


# In[50]:


df.head()


# In[51]:


import pandas as pd


# In[60]:


#The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood
#Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
df_clean = df[df['Borough'] != 'Not assigned']
df_clean.head(30)


# In[62]:


#f a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.
df_clean['Neighborhood']=df_clean['Neighborhood'].replace('Not assigned', df['Borough'])
df_clean.head()


# In[64]:


#Print the number of rows of your dataframe.
print(df_clean.shape)


# In[ ]:




