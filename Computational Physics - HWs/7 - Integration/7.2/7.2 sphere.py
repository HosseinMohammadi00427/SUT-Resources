#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sphere CM
import time
import numpy as np
import random as rnd
T11 = time.time()


def find_mean(f,N,R,P,T):
    """Find the mean of function f(r,phi,theta) in range (0,R) (0,P) (0,T) with N samples (Integration has done on spherical coordinates)"""
    c = 0
    g = lambda r,p,t : (r**2)*np.sin(t)
    for _ in range(N):
        r = rnd.uniform(0,R)
        p = rnd.uniform(0,P)
        t = rnd.uniform(0,T)
        c += (f(r,p,t)*g(r,p,t))
    return c/N
rho0 = 11.8
R= 47
f = lambda r,p,t : r*np.cos(t)*((rho0/(2*R))*r*np.cos(t) +1.5*rho0)
r1,r2 = 0,R
p1,p2 = 0,2*np.pi
t1,t2 = 0,np.pi
N=100000
I = (r2-r1)*(p2-p1)*(t2-t1)*find_mean(f,N,R,p2,t2)
T22 = time.time()
print('R =',R)
print('Rho 0 =',rho0)
print('Numeric value of zCM', round(I/((4/3)*np.pi*rho0*r2**3),6))
print('Real value of zCM:',round(R*0.1,3))
print('Elapsed Time:',round(T22-T11,4))

