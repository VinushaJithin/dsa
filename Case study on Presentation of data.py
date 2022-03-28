#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


#1. Read the dataset to the python environment.

dataset=pd.read_csv(r"C:\Users\jithi\Desktop\Vinu DSA\cars_data.csv")


# In[19]:


dataset


# In[31]:


#2. Check for the null values present in the dataset.

dataset.isnull().values.any()


# In[33]:


#3. Plot a bar graph of male vs female buyers participated in the sales.
sns.countplot(x='Buyer Gender',data=dataset, palette=['#FF0000',"#000000"])


# In[46]:


#4. Find the top 5 cars based on their sales price.
top_5 = dataset.sort_values(by="Sale Price", ascending=False).head()
top_5.plot(x="Model", y="Sale Price", kind="bar", rot=5, fontsize=18)
top_5.head(5)


# In[45]:


#5. Find the least 5 cars based on their Resell price.
least_5 = dataset.sort_values(by="Resell Price", ascending=True).head()
top_5.plot(x="Model", y="Resell Price", kind="bar", rot=5, fontsize=12)
least_5.head(5)


# In[ ]:





# In[ ]:




