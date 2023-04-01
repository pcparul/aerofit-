#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import os


# In[2]:


data=pd.read_csv('aerofit_treadmill.csv')


# In[3]:


data


# In[4]:


data.info()


# In[5]:




import seaborn as sns
sns.countplot(data['MaritalStatus'])
     


# In[6]:


data.nunique()


# In[7]:


sns.countplot(data['Product'])


# In[8]:


sns.boxplot(data['Miles'])


# In[9]:


sns.boxplot(data['Income'])


# In[10]:


#let us see Outliers
data.loc[data['Income'] > 78000]


# In[11]:



temp=data.groupby("Usage")["Miles"].mean()
temp.reset_index()
     


# In[12]:


sns.boxplot(x='Product',y='Income',data=data)


# In[13]:


data.corr()


# In[14]:


sns.heatmap(data.corr(),annot=True)


# In[15]:


sns.lineplot(x='Age',y='Income',data=data,hue='Product')


# In[16]:


sns.boxplot(x='Gender',y='Income',data=data)


# In[17]:


data.groupby('Gender')['Income'].mean()


# In[18]:



# q1=data['Income'].quantile(0.25)
# q3=data['Income'].quantile(0.75)
# iqr=q3-q1
# data=data[(data['Income']>q1-1.5*iqr) & (data['Income']


# In[19]:


sns.boxplot(x='Gender',y='Income',data=data)


# In[20]:


#Convert numerical to  categorical column
data['age_group']=pd.cut(x=data['Age'],bins=[0,18,28,38,48,58,68,100],labels=['0-18','19-28','29-38','39-48','49-58','59-68','69-100'])
     


# In[21]:


data


# In[22]:


sns.countplot(data['age_group'])


# In[23]:


sns.barplot(x='age_group',y='Income',hue='Product',data=data)


# In[24]:


#Probability of customer being male
len(data.loc[data['Gender']=='Male'])/len(data)


# In[25]:



#Contingency Table

#This will give us Marginal probability for each case
temp=pd.crosstab(index=data['Gender'],columns=data['Product'],margins=True, normalize=True)*100
temp


# In[26]:


data.groupby(['Gender','MaritalStatus','Product'])['Miles'].sum().unstack()


# In[27]:


data.groupby(['Gender','MaritalStatus','Product'])['Miles'].sum().unstack().unstack()


# In[28]:


#probability of customer being Female, given she uses KP481 PRODUCT

temp['KP481']['Male']/temp['KP481']['All']


# In[29]:


sns.pairplot(data)


# 
# #Recommendations
# 
# Most people use KP281 which is basic version.
# 
# people buying KP781 are having High income.
# 
# Our product is most popular among age 19-28.We should target these customers.
# 
# People from age 0-18 and '49-58' are buying only cheap products. people with age more than 58 are not buying any product.We can customize prduct to attract these customers.
# 
