#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rnd
import numpy as np
import pylab as plb
N = 2000
data_rho = []
data_theta = []
Dat = []
sigma = 1

f = lambda x : np.sqrt(2)*np.log(1/((x)**sigma))
g = lambda y : 2*np.pi*y
for _ in range(N):
    data_rho.append(f(rnd.uniform(0,1)))
    data_theta.append(g(rnd.uniform(0,1)))
for i in range(N):
    Dat.append(data_rho[i]*np.cos(data_theta[i]))
    Dat.append(data_rho[i]*np.sin(data_theta[i]))
plb.hist(Dat,bins=200)
plb.title('Distribution of random Numbers\n {} numbers'.format(2*N),fontsize=16)
plb.xlabel('Random Number',fontsize=15)
plb.ylabel('Frequency',fontsize=15)

