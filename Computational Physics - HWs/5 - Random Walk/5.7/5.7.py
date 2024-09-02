#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import itertools
T11 = time.time()


def Sign(x):
    """Returns the sign of a int number. for 0 it returns an empty string"""
    if not x:
        return ""
    elif x>0:
        return "+"
    else:
        return "-"
def SignedInt(string,k=0):
    """It recieves an string number and an int and returns their sum as a signed string(the sign + the number)"""
    num = int(string)
    num += k
    String = str(num)
    String = String.replace('+','')
    String = String.replace('-','')
    return Sign(num)+String
    
def is_valid(string):
    """Checks whether string could be a good candidate to a SAW? some cases that checked in this function are obvious non SAWS"""
    Unvalids = ("1234","2341","3412","4123","4321","3214","2143","1432")
    if "13" in string or "31" in string  or "24" in string or "42" in string:
        return False
    for unv in Unvalids:
        if unv in string:
            return False
    return True

    
def all_repetitive_perms(Length,elements="",order=0):
    """A generator object which yields all 4^N sequences of N-step random walk"""
    numbers = ['1','2','3','4']
    if order == Length-1:
        for num in numbers:
            yield num
    else:
        for perm in all_repetitive_perms(Length,elements,order+1):
            for i in numbers:
                yield elements+i+perm
            

####### L is the number of walks ###########3
L = 7
j=0

for seq in all_repetitive_perms(L):
    count = 1
    seq += "0"
    Homes = "|0,0"
    if not is_valid(seq):
        continue
    #print(seq)
    for num in seq:
        #print(Homes)
        m = Homes.rfind("|")
        n = Homes.rfind(",")
        x = Homes[m+1:n]
        y = Homes[n+1:]

        if (( SignedInt(x) +","+ SignedInt(y)) in Homes[:m]):
            count = 0
            break
            
        if num == "1":
            Homes += "|" + SignedInt(x) +","+ SignedInt(y,1)
        elif num == "3":
            Homes += "|" + SignedInt(x) +","+ SignedInt(y,-1)
        elif num == "2":
            Homes += "|" + SignedInt(x,+1) +","+SignedInt(y,0)
        elif num == "4":
            Homes += "|" + SignedInt(x,-1) +","+  SignedInt(y,0)

    j+=count


T22 = time.time()

print('RunTime:',T22-T11)
print('N = {} and SAW = {}'.format(L,j))

