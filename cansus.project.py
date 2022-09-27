#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r"C:\Users\saini\Downloads\6. India Census 2011.csv")
data.head(1)


# ### 1. how will hide the index.

# In[4]:


data.style.hide_index()


# ###  how we can set the caption and heading on dataframe.

# In[ ]:


data.style.set_caption('india cases databases')


# ### 3. show the records with related with the districts - New Delhi,Lucknow,Jaipur.

# In[ ]:


data.head(1)


# In[ ]:


data[(data['District_name'].isin(['New Delhi','Lucknow','Jaipur']))]


# ### 4. calculate the statewise:
# 

# ### a. total number of population

# ### b. total number of population with diff religion.

# In[ ]:


data.head(1)


# In[ ]:


data.groupby('State_name').Population.sum().sort_values(ascending=False)


# In[ ]:


data.columns


# In[ ]:


data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values(by='Hindus')


# ### 5. how many male workers were there in maharashtra in live?

# In[ ]:


data.head(1)


# In[5]:


data[data['State_name']=='MAHARASHTRA']['Male_Workers'].sum()


# ### 6. how to set a column index in the dataframe

# In[ ]:


data.set_index('District_code')


# ### 7.a add a suffix in the column
# ### add a preffix in the column

# In[ ]:


data.head(1)


# In[ ]:


data.add_suffix('_right').head(1)


# In[ ]:


data.add_prefix('left_').head(1)


# In[ ]:




