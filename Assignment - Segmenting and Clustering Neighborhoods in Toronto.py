#!/usr/bin/env python
# coding: utf-8

# In[98]:


postalCode_Canada=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")

df=postalCode_Canada[0]


# In[99]:


df.head()


# In[100]:


import pandas as pd


# In[101]:


#The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood
#Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
df_clean = df[df['Borough'] != 'Not assigned']
df_clean.head(30)


# In[102]:


#f a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.
df_clean['Neighborhood']=df_clean['Neighborhood'].replace('Not assigned', df['Borough'])
df_clean.head()


# In[103]:


#Print the number of rows of your dataframe.
print(df_clean.shape)


# In[108]:


PostCode = pd.DataFrame(df_clean)


# In[109]:


PostCode.to_csv('PostCode.csv')


# In[110]:


import wget
import pandas as pd
import numpy as np


# In[111]:


Geospatial_data = wget.download('https://cocl.us/Geospatial_data')
Coords = pd.read_csv('Geospatial_Coordinates.csv')
Coords.head()


# In[112]:


All = pd.merge(PostCode, Coords)
All.head()


# In[116]:


from geopy.geocoders import Nominatim # convert an address into latitude and longitude values


# In[119]:


#Getthe latitude and longitude values of Toronto with a user_agent tr_explorer
address = 'Toronto'

geolocator = Nominatim(user_agent="tr_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto {}, {}.'.format(latitude, longitude))


# In[121]:


import folium # map rendering library


# In[123]:


# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(All['Latitude'], All['Longitude'], All['Borough'], All['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


# In[ ]:




