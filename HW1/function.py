import random
import math

def func(a,b):
    #return  a*math.exp(-a*a-b*b)

    #------
    if a>=0:
        return a*math.exp(-a)*math.sin(b)
    else:
        return a*math.exp(a)*math.sin(b)



