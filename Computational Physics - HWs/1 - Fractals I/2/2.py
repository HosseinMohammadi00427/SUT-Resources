import math
import pylab as plb
plb.rcParams['figure.figsize'] = 10,7

L=2
lvl = 10

def Rotate(Pts,theta,Cent):
    new_Pts = []
    theta = math.radians(theta)
    for P in Pts:
        x = (P[0]-Cent[0])*math.cos(theta) - (P[1]-Cent[1])*math.sin(theta)
        y = (P[0]-Cent[0])*math.sin(theta) + (P[1]-Cent[1])*math.cos(theta)
        new_Pts.append((x+Cent[0],y+Cent[1]))
    return new_Pts

def HW(Pts,n,m):
    for k in range(n):
        Pts = Rotate(Pts,-45*m,(0,0))
        PtsCopy = Pts.copy()
        PtsCopy = Rotate(PtsCopy,-90,PtsCopy[-1])
        Pts.extend(PtsCopy[::-1])
    return Pts

Pts = [(-L,L),(0,0),(L,L)]
Pts1 = HW(Pts,lvl,1)
Pts2 = Rotate(Pts1,-45*4,Pts1[-1])
plb.plot([k[0]for k in Pts1],[k[1]for k in Pts1],c='r')
plb.plot([k[0]for k in Pts2],[k[1]for k in Pts2],c='b')