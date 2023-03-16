#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Se importan librerias de operaciones matematicas, de tratamiento de datos y de graficos 
import numpy as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#se leen los datos
datos = pd.read_csv(r'C:\Users\Andres\Documents\Python\vehiculos.csv')
datos


# In[20]:


#Graficamos los datos
plt.figure(figsize=(8,5))
x_datos, y_datos = (datos['id'].values, datos['long'].values)#Se toman los datos
plt.plot(x_datos, y_datos,'ro')# Se grafica
plt.xlabel('id')
plt.ylabel('long')
plt.show()


# In[21]:


#Ejemplo de una funcion logistica para verificar el comportamiento
x= np.arange(-5.0, 5.0, 0.1)
y= 1.0/(1.0 + np.exp(-x))
plt.plot(x,y)
plt.ylabel('id')
plt.xlabel('long')
plt.show()


# In[ ]:




