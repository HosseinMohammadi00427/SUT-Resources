#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pylab as plb
import random as rand
plb.rcParams['figure.figsize'] = 14,8  # U can change the size of bar plot here

N = 200       # The number of Rooms
t = 500000   # Hom many seeds?
d = 1         # Iteration of Code
StopNo = 4    # Number of stops
Samples = [] 
Ws = [[] for i in range(StopNo+1)]
Hs_ave = []
Stops = np.array([t/(2**k) for k in range(StopNo,-1,-1)],int)

def Visualize(xAxis,width,n,*args):
    for i,LIST in enumerate(args):
        if i==0:
            plb.bar(xAxis,LIST,width)
        else:
            bottom = [[args[j][k] for k in range(n)] for j in range(0, len(args) ) if j<i]
            bottom = np.array(bottom)
            Key = np.zeros(n,int)
            for B in bottom:
                Key += B
            plb.bar(xAxis,LIST,width,bottom = Key.tolist())
            plb.title("The distribution of particles in all Places",fontsize=16)
            plb.xlabel("Place",fontsize=14)
            plb.ylabel("Cumulative Count of Particles",fontsize=14)
    plb.show()


for Iterations in range(0,d):   # Runs the code d times just for averaging over it
    W_Counter = 0
    Samples = []
    Rooms = [0]*N
    for i in range(t+1):        # Placing Atoms on surface
        r = rand.randint(0,N-1)
        Rooms[r] += 1 
        if i in Stops:
            Samples.append(Rooms[::1]) #Why do that? ;)
            (Ws[W_Counter]).append( np.sqrt(np.var(Rooms)) )
            Hs_ave.append(i/N)
            W_Counter+=1

# if you want to see the visualization just uncomment below :)
Visualize(np.arange(N),1,N,*Samples)
#print('Average of h is : {:.3f}'.format(t/N))
for No,data in enumerate(Samples):
    print('In {} level of {} iterations w(t) is {:.3f}'.format(Stops[No],t,np.sqrt(np.var(data))))


"""Collary:
why the height in bar plot is not t/N
because the bar plot is drawn cumulative if we draw instead:
Visualize(np.arange(N),1,N,Samples[-1])
You'll see that the average of h is exactly t/N :)
"""


# In[5]:


plb.rcParams['figure.figsize'] = 8,6
dynamic_data = []
for k in range(StopNo+1):
    dynamic_data.append((Stops[k],round(np.mean(np.array(Ws[k],dtype = float)),3 )))
Xs = np.array([d[0] for d in dynamic_data])
Ys = np.array([d[1] for d in dynamic_data])




plb.scatter(np.log10(Xs),np.log10(Ys),label="Data points of W(t)")
plb.legend()
plb.title("Scatter plot of Data points of W(t) + The best fitted Line in Random Ballistic Deposition Problem",fontsize=16)
plb.xlabel("log(t) (which is the number of all droped seeds or time)",fontsize=14)
plb.ylabel("Log(W) (The variance of mean Data Points)",fontsize=14)
Xs = np.log10(Xs)
Ys = np.log10(Ys)
p = np.polyfit(Xs,Ys,1)

p = np.poly1d(p) # (Betta)x+A
A=10**(p.c[1])
plb.plot(Xs,p(Xs),label="The Best fitted Line",c="r")
plb.legend()
print("\u03B2 is {:.6f} and A is {:.6f} in equation: W ~ At^\u03B2".format(p.c[0],A))



"""
Some typical Values for betta and A(the constant) for 5000000 iteration:
A = 0.0681 and betta = 0.5011
A = 0.0662 and betta = 0.5044
A = 0.0807 and betta = 0.4902
A = 0.0470 and betta = 0.5323
A = 0.0774 and betta = 0.4933
Their Variance will be:
var(betta) = 0.0002
var(A) = 0.0001
"""

