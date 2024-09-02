#!/usr/bin/env python
# coding: utf-8

# In[14]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()


#Chaos
import random
chaos = lambda x,r: 4*r*x*(1-x)
Data = []

for r in np.linspace(0,1,201):
    x = random.random()
    for _ in range(100):
        x = chaos(x,r)
    Data.append([])
    Data[-1] = [x]
    for i in range(50):
        Data[-1].append(chaos(Data[-1][-1],r))
        
        
i=0
get_ipython().run_line_magic('matplotlib', 'qt')
plb.rcParams['figure.figsize'] = 12,8
for K in np.linspace(0,1,201):
    plb.scatter([K]*51,Data[i],color="black",marker=".")
    i+=1



print(time.time()-Time_1)

