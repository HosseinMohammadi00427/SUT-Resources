#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import numpy as np
import pylab as plb

plb.rcParams['figure.figsize'] = 8,6

Time_1 = time.time()


#Verlet Algorithm

a,b = 0,20*np.pi
h = 0.15
steps2 =int((b-a)//h) + 1
t0,x0,x1 = 0,0,0.3

Acc = lambda x : -x

Xs2 = [x0,x1]
Vs = []

for i in range(1,steps2):
    Xs2.append(2*Xs2[-1] - Xs2[-2] + Acc(Xs2[-1])*(h**2))
    
for j in range(1,steps2-1):
    Vs.append((Xs2[j-1]+Xs2[j+1])/2/h)
plb.plot(np.linspace(a,b,steps2+1),Xs2)
#plb.plot(np.linspace(a,b,1000),2*np.sin(np.linspace(a,b,1000)))

plb.figure(2)
plb.plot(Xs2[:-3],Vs,label="Data points")
plb.legend()
plb.title('V versus X for Verlet\nh=0.05 and 10 cycles',fontsize=16)
plb.xlabel('X(Position)',fontsize=15)
plb.ylabel('V(elocity)',fontsize=15)



print(time.time()-Time_1)

