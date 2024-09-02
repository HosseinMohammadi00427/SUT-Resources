#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random as rnd
import numpy as np
import pylab as plb
N = 10000
k = 9
Datas = []
S=0
for _ in range(N):
    Datas.append(rnd.randint(0,k))
Datas = np.array(Datas)
Fours = np.argwhere(Datas == 4).flatten()
new_rands = [Datas[i-1] for i in Fours]
plb.hist(new_rands,bins=k+1,width=1)

plb.title('Distribution for N ={}'.format(N),fontsize=16)
plb.xlabel('Numbers',fontsize=15)
plb.ylabel('Frequency',fontsize=15)

