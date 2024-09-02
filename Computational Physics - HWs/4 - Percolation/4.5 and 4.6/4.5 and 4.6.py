#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import numpy as np
import pylab as plb
import matplotlib
import time

T11 = time.time()
plb.rcParams['figure.figsize'] = 10,10

SIZE = 10
pvals = np.linspace(0.0,0.4,num=5)
pvals = np.append(pvals,np.linspace(0.42,0.62,num=10))
pvals = np.append(pvals,np.linspace(0.63,0.1,num=5))
d = 1
Xs = []
Ys = []


def Where_It_Points(L,x):
    while L[x] != x:
        x = L[x]
    return L[x]

def ConnectedToInfIsland(net,L,val):
    #How rewrite it to use before coloring?
    realm = Where_It_Points(L,val)
    for num in net[:,0]:
        if num and Where_It_Points(L,num) == realm:
            break
    else:
        return False 
    for num in net[:,-1]:
        if num and Where_It_Points(L,num) == realm:

            return True
    else:
        return False
    

def Perculated(net,L):
    dim = net.shape[0]
    A = set([net[i,0] for i in range(dim)])
    B = set([net[i,dim-1] for i in range(dim)])
    A.discard(0)
    B.discard(0)
    A = np.array(list(A))
    B = np.array(list(B))
    dimA , dimB = A.shape[0],B.shape[0]
    for s in range(dimA):
        A[s] = Where_It_Points(L,A[s])
    for k in range(dimB):
        B[k] = Where_It_Points(L,B[k])   
    if len(np.intersect1d(A,B)):
        return True
    return False

#Let's Do it
def Rearrange_Matrix(Mat,L):

    non0 = np.count_nonzero(L)
    Coupling_color_List = [[] for s in range(non0+1)]

    for i,color in enumerate(L.tolist()):
        if not color:
            continue
        if L[i] == i:
            Coupling_color_List[i].append(color)
        else:
            for k in range(non0):
                if color in Coupling_color_List[k+1]:
                    Coupling_color_List[k+1].append(i)
                    break
            else:
                Coupling_color_List[i].append(i)
                Coupling_color_List[i].append(color)
    
    while [] in Coupling_color_List:
        Coupling_color_List.remove([])
    non0 = len(Coupling_color_List)
    
    for w in range(non0):
        for t in range(non0):
            A = set(Coupling_color_List[t])
            B = set(Coupling_color_List[w])
            if A & B and w != t:
                C = A | B
                Coupling_color_List.remove(Coupling_color_List[t])
                Coupling_color_List.insert(t,list(C))
                Coupling_color_List.remove(Coupling_color_List[w])
                Coupling_color_List.insert(w,[])

    for elem in Coupling_color_List: 
        if elem:
            for j in elem:
                Mat[Mat == j] = min(elem)
    return Mat

def Gyr_rad(net,L,val):
    
    """Just give me non-infinite clusters :)"""
    
    Alias = np.zeros((len(L)),'int32')
    Alias[0] = val
    
    ances = Where_It_Points(L,val)
    i=1
    
    for j in range(len(L)):
        if L[j] and Where_It_Points(L,L[j]) == ances:
            Alias[i] = j
            i+=1

    Alias = np.unique(np.setdiff1d(Alias,np.array([0])))
    SumX , SumY , Totlen = 0,0,0
    for al in Alias:
        Places = np.argwhere(net == al)
        Totlen += np.count_nonzero(net == al)
        for Point in Places:
            SumX += Point[0]
            SumY += Point[1]
    
    X_Center , Y_Center = SumX/Totlen , SumY/Totlen
    SumR = 0
    for al in Alias:
        Places = np.argwhere(net == al)
        for Point in Places:
            SumR += (Point[0]-X_Center)**2 + (Point[1]-Y_Center)**2

    return  np.sqrt(SumR/Totlen)



def NonInfIsland(net,L):

    UNIQUE = np.unique(net)
    NonInfs = np.zeros((len(L)),'int32')
    j=0
    for un in UNIQUE:
        if un:
            if not ConnectedToInfIsland(net,L,un) and Where_It_Points(L,un) not in NonInfs:
                NonInfs[j] = Where_It_Points(L,un)
                j+=1

    return np.unique(np.setdiff1d(NonInfs,np.array([0])))
    
def Give_me_the_Phsi (net,L):
    NonInfs = NonInfIsland(net,L)
    Sum = 0
    for n in NonInfs:
        Sum += Gyr_rad(net,L,n)
    try:
        return Sum /(len(NonInfs))
    except ZeroDivisionError:
        return 0

#Hoshen kopelman
for p in pvals:
    Mean_Psi = 0
    for _ in range(d):
        C = 1
        L = np.zeros((SIZE*SIZE//2+1,),'int64') #(SIZE*SIZE//2)
        S = np.zeros(SIZE*SIZE//2+1,'int64')
        Island_Matrix = np.zeros((SIZE,SIZE),'int32')
        net = np.random.rand(SIZE,SIZE)
        net[net > p] = 0
        net[net != 0] = 1
        net = net.astype('int8')

        for j in range(SIZE):
            for i in range(SIZE):
                if net[i,j]:
                    if i == 0:
                        if j == 0:
                            Island_Matrix[i,j] = C
                            L[C] = C
                            S[C] +=1
                            C+=1
                        elif net[i,j-1]:
                            Island_Matrix[i,j] = Island_Matrix[i,j-1]
                            S[L[Island_Matrix[i,j-1]]] +=1
                        else:
                            Island_Matrix[i,j] = C
                            L[C] = C
                            S[C] +=1
                            C+=1
                    elif j == 0:
                        if net[i-1,j]:
                            Island_Matrix[i,j] = Island_Matrix[i-1,j]
                            S[L[Island_Matrix[i-1,j]]] +=1
                        else:
                            Island_Matrix[i,j] = C
                            L[C] = C
                            S[C] +=1
                            C+=1
                    else:
                        Min = min({Island_Matrix[i-1,j],Island_Matrix[i,j-1]})
                        Max = max({Island_Matrix[i-1,j],Island_Matrix[i,j-1]})
                        MinRef = Where_It_Points(L,Min)
                        MaxRef = Where_It_Points(L,Max)
                        if Max == 0:
                            Island_Matrix[i,j] = C
                            L[C] = C
                            S[C] +=1
                            C+=1

                        elif not Min and Max:
                            Island_Matrix[i,j] = Max
                            S[L[MaxRef]] +=1

                        elif Max == Min:
                            Island_Matrix[i,j] = Max
                            S[L[MaxRef]] +=1

                        elif Max != Min:

                            MinRef = Where_It_Points(L,Min)
                            MaxRef = Where_It_Points(L,Max)

                            Island_Matrix[i,j] = Min
                            if L[MaxRef] != L[MinRef]:
                                S[L[MinRef]] += S[L[MaxRef]]
                                L[MaxRef] = L[MinRef]
                            S[L[MinRef]] +=1
        #Dont uncomment below because the runtime will add...
        #Island_Matrix = Rearrange_Matrix(Island_Matrix,L)

        Mean_Psi += Give_me_the_Phsi(Island_Matrix,L)  
    Xs.append(p)
    Ys.append(Mean_Psi/d)    
np.set_printoptions(threshold=sys.maxsize)            

#Uncomment Below to see the Latticd 
#cmap = matplotlib.colors.ListedColormap(['white',"black",'skyblue','tan','thistle','teal','sandybrown','red','coral','blueviolet','khaki','ivory','deeppink','salmon','tomato','purple','orange','green','yellow','grey','blue','cyan','lime','olive','gold','maroon','pink','brown','indigo']*101)
#Island_Matrix = Rearrange_Matrix(Island_Matrix,L)
#plb.imshow(Island_Matrix,cmap=cmap)
#print(Island_Matrix[0],'\n',Island_Matrix[-1])

T22 = time.time()
print(T22 - T11)

