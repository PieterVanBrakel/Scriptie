#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Installing new version of seaborn library

pip install -U seaborn


# In[2]:


# Load relevant libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Loading the dataset in a dataframe

df = pd.read_csv('WELFake_Dataset.csv')


# In[4]:


# Print the dataframe shape

df.shape

# This means there are 72134 rows and 4 columns


# In[5]:


# Print de column namen

df.columns

# The columns are the article index number, article title, rticle text and the true/false article label.


# In[6]:


# Print the numerical info of instances. 

df.index

# There are this 72134 instances.


# In[7]:


# Print the first 5 articles

df.head()


# In[8]:


# Print the last 3 articles

df.tail(3)


# In[9]:


# Print general info about the columns

df.info()


# In[10]:


# Print statistical information about the dataset. This is basically useless for this dataset.

df.describe()


# In[11]:


# Print missing values

df.isnull().sum()

# This means 558 article titles and 39 article texts are missing. All true/false labels are included.
# You might need to clean missing values from your dataset. Ask this to your professor.


# In[12]:


# Print the y label (true/false) statistics

print("The amount of true news articles:",(df.loc[:,"label"] == 1).sum())
print("The amount of fake news articles:",(df.loc[:,"label"] == 0).sum())


# In[13]:


# Plot the distribution of true news and fake news

plt.figure(figsize = (8,5))
sns.countplot(x = df['label'], palette = 'Set1', alpha = 0.8)
plt.title('Distribution of Fake - 0 /Real - 1 News')


# In[14]:


df.loc[1]


# In[18]:


df.iloc[2,1]


# In[ ]:




