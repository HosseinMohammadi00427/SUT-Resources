#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pylab as plb
import matplotlib
plb.rcParams['figure.figsize'] = 6,6


def existsPath(net, i=0, j=0,start=True):
    dim = net.shape[0]
    if start:
        for k in range(dim):
            if net[i][k]:
                j = k
                break
        else:
            return False
           
    if j >=dim or j<0:
        return False
    if i >= dim-1:
        return True
    
    if 2 not in [net[i][k] + net[i+1][k]  for k in range(dim)]:
        return False
    
    if net[i][j] and net[i+1][j]:
         return existsPath (net, i+1, j,False)
    
    elif net[i][j] and  j<dim-1 and net[i][j+1] :
         return existsPath (net, i, j+1,False)
    
    elif net[i][j] and  j>0 and net[i][j-1] :
         return existsPath (net, i, j-1,False)
    else:
        return False
        

L = 3
p = .59
net = np.random.rand(L,L)
net[net > p] = 0
net[net != 0] = 1
net = net.astype('int8')
print(net)
plb.imshow(net,cmap="binary")
#print(existsPath(net))

