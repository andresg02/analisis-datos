#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Documents/Python/vehiculos.csv")
datos


# In[ ]:


datos=pd.read_csv("Documents/Python/vehiculos.csv")


# In[3]:


datos


# In[5]:


processdatos=pd.read_csv("Documents/Python/vehiculos.csv")
processdatos.head()


# In[11]:


fig=plt.figure(figsize=(14,14))
plt.scatter(processdatos['id'],processdatos['region'])
plt.plot(processdatos['id'],processdatos['region'])
plt.xlabel('id')
plt.ylabel('region')
plt.grid()


# In[ ]:





# In[ ]:





# In[ ]:




