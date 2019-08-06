#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def sn_random_numbers(shape,antithetic=True,moment_matching=True,fixed_seed=False):
    if fixed_seed:
        np.random.seed(1000)
    if antithetic:
        ran=np.random.standard_normal((shape[0],shape[1],shape[2]//2))
        ran=np.concatenate((ran,-ran),axis=2)
    else:
        ran=np.random.standard_normal(shape)
    if moment_matching:
        ran-=np.mean(ran)
        ran/=np.std(ran)
    if shape[0]==1:
        return ran[0]
    else:
        return ran


# In[ ]:





# In[ ]:




