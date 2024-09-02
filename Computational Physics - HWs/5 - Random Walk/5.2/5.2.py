#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pylab as plb
import random

p = 0.5
q = 1-p
N = 400
SIZE = 1000

Places = np.zeros(SIZE)
Places[SIZE//2] = 1

iters = 1000
position = 0
Save = []


def E(X,Y,p = 1):
    """It's mathematical function 'Expected Value' which is used in finding sigma (std)"""
    e = 0
    for s in range(len(X)):
        e += (X[s]**p)*Y[s]
    return e

def variance(X,Y):
    """returns std of X and Y (by defenition)"""
    """ Notice that I could find use numpy built in functions but I didn't know what it do insider the function np.std()"""
    return E(X,Y,p = 2) - E(X,Y,p = 1)**2

for _ in range(iters):
    position = 0
    for i in range(N):
        rand = random.random()
        if rand<p:
            position +=1
        else:
            position -=1
    Save.append(position)
average = (sum(Save)/iters)
std = (np.var(Save))
# Uncomment Below for deterministics MODE :)
"""
for i in range(N):
    avail_homes = np.argwhere(Places)
    for av in avail_homes:
        Places[av-1] += q*Places[av]
        Places[av+1] += p*Places[av]
        Places[av] = 0
        


Xs = np.array(range(SIZE))
Xs = Xs - SIZE//2

Positivs = np.argwhere (Places>0)
U = [x-SIZE//2 for x in Positivs]
V = [Places[x] for x in Positivs]
plb.plot(U,V,linestyle = "--",label='connected data points')

plb.title('the distribution of places for p = {} and q = {} with {} steps'.format(round(p,3),round(q,3),N))
plb.legend()
plb.xlabel('(x) distance along an axis',fontsize=16)
plb.ylabel('P  (Probablity)',fontsize=16)
"""
print('p = {} , q = {} , N(steps) = {} \nLattice size = {} , iterations = {}'.format(p,round(q,3),N,SIZE,iters))
print('\n                ***Mean***\n<x(t)> = (p-q)*N (Theoritical)  =  ',round((p-q)*N,4),'\nBy averaging on P(x):',round(average,1))
print('\n             ***Variance***\n\u03c3^2 = 4Npql^2 (Theoritical) = :',round(4*N*p*q,4),'\nAnd By using np.var():',round(average,3))

