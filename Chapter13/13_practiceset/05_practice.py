#Practice task no 05

from functools import reduce

list = [100,2,3,4,5,6,7,8,9]

def greater(a,b):
    if (a>b):
        return a
    else:
        return b
    

R = reduce(greater,list)
print(R)


