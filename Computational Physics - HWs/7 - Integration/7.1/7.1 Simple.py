#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple Sampling
import time
import numpy as np
import random as rnd
T11 = time.time()

f = lambda x : np.exp(-x**2)
a,b = 0,2
N=100000

def find_mean(f,a,b,N):
    """ّFind The mean of function f(x) in the interval (a,b) by N samples."""
    c = 0
    for _ in range(N):
        x = rnd.uniform(a,b)
        c += f(x)
    return c/N


I = (b-a)*find_mean(f,a,b,N)
T22 = time.time()
print( 'Simple Sampling' )
print( 'Integral value is: ',round(I,9) )
print('Time elapsed:',round(T22-T11,5),' s')

