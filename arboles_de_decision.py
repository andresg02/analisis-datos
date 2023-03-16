#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[11]:


datos = pd.read_csv("Documents/Python/vehiculos.csv")


# In[4]:


datos.head(5)


# In[13]:


datos.info()


# In[14]:


#Variables predictoras
X = datos.iloc[:,1:26]

#Variable a predecir
Y = datos.iloc[:,0]

#Mostramos las primeras cinco filas
X.head()

