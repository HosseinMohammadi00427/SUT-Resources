#!/usr/bin/env python
# coding: utf-8

# In[15]:


#2d random walk
import numpy as np
import pylab as plb
import random

p1 = 0.25
p2 = 0.25
p3 = 0.25
p4 = 1 - (p1+p2+p3)
N = 500
r_list = []
iterations = 5000
Place = np.zeros((2),int)
dim = 2


def E(X,Y,p = 1):
    """It's mathematical function 'Expected Value' which is used in finding sigma (std)"""
    e = 0
    for s in range(len(X)):
        e += (X[s]**p)*Y[s]
    print(e)
    return e
def variance(X,Y):
    """returns std of X and Y (by defenition)"""
    return E(X,Y,p = 2) - E(X,Y,p = 1)**2

for _ in range(iterations):
    Place = np.zeros((2),int)
    for i in range(N):
        rand = random.random()
        if 0<rand<p1:
            Place[1] += 1
        elif p1<rand<p1+p2:
            Place[0] += 1
        elif p1+p2<rand<p1+p2+p3:
            Place[1] -= 1
        else:
            Place[0] -= 1
    r_list.append(Place[0]**2+Place[1]**2)

print("Probablity: up = {} / right = {} / down = {} /\nleft = {}  N(steps) = {} and iterations = {}".format(p1,p2,p3,round(p4,2),N,iterations))
print("\n              ***Mean***\n       <r^2> by np.mean() = ",np.mean(r_list))
#Regularly U should find sigma by E(x^2) -E(x)^2
print("       Theoritical Prediction = ",np.sqrt(np.var(r_list)))

