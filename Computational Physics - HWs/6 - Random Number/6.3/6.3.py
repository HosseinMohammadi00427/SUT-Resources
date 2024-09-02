#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random as rnd
import numpy as np
import pylab as plb

iters = 100000
N = 10
k = 5
val = 0
temp = []
for _ in range(iters):
    val = 0
    for __ in range(N):
        val+= rnd.uniform(-k,k)
    temp.append(val)
    
plb.hist(temp,bins=100)
plb.title('Distribution for N ={} and {} iterations'.format(N,iters),fontsize=16)
plb.xlabel('Sum of Numbers',fontsize=15)
plb.ylabel('Frequency',fontsize=15)

