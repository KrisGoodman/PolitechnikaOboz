import matplotlib.pyplot as plt
from sympy import *

def Euler(f, h, x0, y0, xn):
    listx=[]
    listx.append(y0)
    i=x0
    while(i<xn):
        y0 = y0 + h * f.subs({x:x0, y:y0})
        x0 = x0 + listx.append(y0)
        i+=h
        i=round(i,5)
    return listx

def Eulerint (f , h, x0, y0, xn):
    listx=[]
    i = 0
    j = 0
    k = 1/h
    while (i<xn):
        y0 = y0 + h * f.subs({x:x0, y:y0})
        x0 = x0 + listx.append(y0)
        i+=h
        j+=1
        if(j==k):
            listx.append(y0)
            j=0
        return listx