#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# load the tips dataset
df = sns.load_dataset("tips")


# In[4]:


# Print the first 5 rows of the dataset
print(df.head())


# In[5]:


# Print the summary statistics of the dataset
print(df.describe())


# In[6]:


# Create a histogram of the 'total_bill' column
sns.histplot(data=df, x='total_bill')
plt.show()


# In[7]:


# Create a scatter plot of 'total_bill' vs 'tip'
sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()


# In[8]:


# Create a box plot of 'day' vs 'total_bill'
sns.boxplot(data=df, x='day', y='total_bill')
plt.show()


# In[ ]:




