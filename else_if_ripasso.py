#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy.random import randn


# In[18]:


randn ()


# In[49]:


answer = None 
x = randn()
if x > 1:
    answer = "Greater than 1"
print(x)
print(answer)


# In[60]:


answer = None 
x = randn()
if x > 1:
    answer = "Greater than 1"
else: 
    answer = "Less than 1"
print(x)
print(answer)


# In[66]:


#nested statements 
answer = None 
x = randn()
if x > 1:
    answer = "Greater than 1"
else: 
    if x >= -1:
        answer = "Beetween -1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)


# In[73]:


#chained statements 
answer = None 
x = randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
    answer = "Beetween -1 and 1"
else:
    answer = "Less than -1"
print(x)
print(answer)


# ---

# In[75]:


import numpy as np
from numpy.random import randn


# In[80]:


randn ()


# In[94]:


answer = None
x = randn()
if x > 1: 
    answer = ("Greater than 1 ")
print (x)
print (answer)


# In[97]:


answer = None
x = randn()
if x > 1: 
    answer = ("Greater than 1")
else:
    if x < 1:
        answer = ("Lass than 1")
print (x)
print (answer)


# In[120]:


answer = None
x = randn()
if x > 1: 
    answer = ("Greater than 1")
elif x >= -1:
    answer = ("Between -1 and 1")
else:
    answer = ("Lass than 1")
print (x)
print (answer)


# In[ ]:




