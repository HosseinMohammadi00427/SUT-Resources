#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Simple Sampling
import numpy as np
import random as rnd
import time
T11 = time.time()

def arbit_dist_random(G_1,a,b):
    """Generates Random number with specified distribution in specified interval (you must pass to it G^-1)"""
    rand_num = G_1(rnd.uniform(0,1))
    while (a> rand_num or b<rand_num):
        rand_num = G_1(rnd.uniform(0,1))
    return rand_num

def find_mean(f,g,G_1,a,b,N):
    """Returns Mean of a function f in interval (a,b) with Random numbers that have g distribution"""
    c = 0
    for _ in range(N):
        x = arbit_dist_random(G_1,a,b)
        c += (f(x)/g(x))
    return c/N

f = lambda x : np.exp(-x**2)
a,b = 0,2
N=100000

I = (1-1/(np.exp(2)))*find_mean(f,lambda x:np.exp(-x),lambda x: -np.log(x),a,b,N)
T22 = time.time()

print( 'ُSmart Sampling' )
print( 'Integral value is: ',round(I,9) )
print('Time elapsed:',round(T22-T11,5),' s')

