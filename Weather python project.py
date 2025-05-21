#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd


# In[2]:


data = pd.read_csv('Weather python project.csv')


# In[3]:


data


# In[4]:


data.head(5)


# In[5]:


data.tail(5)


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[13]:


data.dtypes


# In[14]:


data['Weather'].unique()


# In[15]:


data.nunique()


# In[16]:


data['Weather'].nunique()


# In[17]:


data.count()


# In[18]:


data['Weather'].count()


# In[19]:


data['Weather'].value_counts()


# In[20]:


data.info()


# # Q1. Find all the unique 'Wind Speed' values in the data.

# In[22]:


data.head(2)


# In[23]:


data.nunique()


# In[24]:


data['Wind Speed_km/h'].unique()


# In[25]:


data['Wind Speed_km/h'].nunique()


# # Q2. Find the number of times when the 'Weather is exactly clear'

# In[26]:


data.head(2)


# In[27]:


data['Weather'].value_counts()


# In[29]:


#data.head(2)
data['Weather'] == 'Clear'


# In[30]:


data[data['Weather'] == 'Clear']


# In[32]:


data.groupby('Weather').get_group('Clear')


# # Q3. Find the number of times when the 'Wind Speed was exactly 4km/h'

# In[33]:


data.head(2)


# In[34]:


data['Wind Speed_km/h'] == 4


# In[35]:


data[data['Wind Speed_km/h'] == 4]


# # Q4. Find out all the Null Values in the data.

# In[36]:


data.isnull()


# In[37]:


data.isnull().sum()


# In[38]:


data.notnull().sum()


# # Q5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'

# In[39]:


data.head(2)


# In[42]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[43]:


data.head(2)


# # Q6 What is the mean 'Visibility' ?

# In[44]:


data.head(2)


# In[45]:


data.Visibility_km.mean()


# # Q7. What is the Standard Deviation 'Pressure' in this data?

# In[46]:


data.Press_kPa.std()


# # Q8. What is the Variance of 'Relative Humidity' in this data?

# In[47]:


data['Rel Hum_%'].var()


# # Q9. Find all instances when 'Snow' was recorded.

# In[48]:


data.head(2)


# In[49]:


data['Weather Condition'].value_counts()


# In[50]:


data[data['Weather Condition'] == 'Snow']


# In[53]:


data[data['Weather Condition'].str.contains('Snow')]


# # Q10. Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'

# In[54]:


data.head(2)


# In[55]:


data[ (data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25) ]


# # Q11. What is the mean value of each column against each 'Weather Condition '?

# In[56]:


data.head(2)


# In[61]:


data.groupby('Weather Condition').mean(numeric_only=True)


# # Q12. What is the minimum & maximum value of each column against each 'Weather Condition'?

# In[63]:


data.head(2)


# In[64]:


data.groupby('Weather Condition').min()


# In[65]:


data.groupby('Weather Condition').max()


# # Q13. Show all the records where Weather Condition is Fog.

# In[67]:


data[ data['Weather Condition'] == 'Fog' ]


# # Q14. Find all instances when 'Weather is Clear' or 'Visibility is over 40'.

# In[68]:


data.head(2)


# In[71]:


data[ (data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40) ]


# # Q15. Find all instance when:

# # A. 'Wheather is clear' and 'Relative Humidity is greater than 50'

# # or

# # B. 'Visibility is above 40'

# In[72]:


data.head(2)


# In[73]:


data[ (data['Weather Condition'] == 'Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km'] >40) ]


# In[ ]:





# In[ ]:




