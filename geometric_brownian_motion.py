#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


from sn_random_numbers import sn_random_numbers


# In[5]:


from simulation_class import simulation_class


# In[22]:


class geometric_brownian_motion(simulation_class):
    
    def __init__(self,name,mar_env,corr=False):
        super(geometric_brownian_motion,self).__init__(name,mar_env,corr)
    
    def update(self,initial_value=None,volatility=None,final_date=None):
        if initial_value is not None:
            self.initial_value=initial_value
        if volatility is not None:
            self.volatility=volatility
        if final_date is not None:
            self.final_date=final_date
        self.instrument_values=None
    
    def generate_path(self,fixed_seed=False,day_count=365):
        if self.time_grid is None:
            self.generate_time_grid()
        M=len(self.time_grid)
        I=self.paths
        paths=np.zeros((M,I))
        paths[0]=self.initial_value
        if not self.correlated:
            rand=sn_random_numbers((1,M,I),fixed_seed=fixed_seed)
        else:
            rand=self.random_numbers
        short_rate=self.discount_curve.short_rate
        
        for t in range(1,len(self.time_grid)):
            if not self.correlated:
                ran=rand[t]
            else:
                ran=np.dot(self.cholesky_matrix,rand[:,t,:])
                ran=ran[self.rn_set]
            dt=(self.time_grid[t]-self.time_grid[t-1]).days/day_count
            
            paths[t]=paths[t-1]*np.exp((short_rate-0.5*self.volatility**2)*dt+
                                      self.volatility*np.sqrt(dt)*ran)
        self.instrument_values=paths


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




