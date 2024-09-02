#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random as rnd
import numpy as np
import pylab as plb
plb.rcParams['figure.figsize'] = 9,6

N = 600
k = 9
Datas = []
iters = 1000
S=0

for _ in range(iters):
    Datas = []
    for j in range(N):
        a = rnd.randint(0,k)
        Datas.append(a)
    Datas = np.array(Datas)
    Counts = np.array([len(Datas[Datas == i])for i in range(k+1)],int)
    Counts = Counts - N//10
    S+= np.sqrt(np.var(Counts))/N
print('mean of sigma is:',S/iters)


"""
plb.hist(Datas,bins=k+1,width=1)
plb.title("Histogram of random Numbers\nUniform distribution with N = {}".format(N),fontsize=16)
plb.xlabel('Numbers',fontsize=15)
plb.ylabel('Frequency',fontsize=15)
"""

