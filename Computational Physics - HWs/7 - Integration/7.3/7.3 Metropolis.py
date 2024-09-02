#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Metropolis
import numpy as np
import random as rnd
import pylab as plb
p = lambda x: np.exp(-x**2)
N = 100000
x = 0
y = 0
dat = []
acr = 0
j=4

def variance(data):
    """Returns the std(standard deviation) of data"""
    data = np.array(data)
    return(np.mean(data**2) - np.mean(data)**2)


def Correlation(data,j):
    """Finds the Autocorrelation between samples (data) with distance j"""
    data = np.array(data)
    A = 0
    B = 0
    for i in range(len(data)):
        if i+j < len(data):
            A += data[i]*data[i+j]
            B += data[i+j]

    A/= (len(data)-j)
    B/= (len(data)-j)
    return (A - np.mean(data)*B)/variance(data)



for _ in range(N):
    y = x + rnd.uniform(-1,1)
    if rnd.random() < p(y)/p(x):
        dat.append(y)
        acr+=1
        x=y
#Uncomment bellow to see the distribution
#plb.hist(dat,bins=150,normed=1)
print('Acceptance Rate:',acr/N)

print('C(data,{}) = '.format(j),Correlation(dat,j))

