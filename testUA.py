#!/usr/bin/env python
# coding: utf-8



# In[14]:


import httpagentparser as parser


# In[15]:


def detect(ua) :
    a = parser.simple_detect(ua)
    return a


# In[17]:

x = "Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/14D27 Safari/602.1"
print(detect(x))


# In[ ]:




