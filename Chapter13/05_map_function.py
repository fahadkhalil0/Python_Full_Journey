from functools import reduce
# #Map function in python

List = [1,2,3,4,5]

# sqrlist = lambda x: x*x

# Sqr = map(sqrlist, List)
# print(Sqr)
# print(list(Sqr))

#Filter function in python

def odd(n):
    if (n%2 != 0):
        return True
    return False

onlyOdd = filter(odd, List)
print(list(onlyOdd))


# Reduce filter in python
def sum(x,y):
    return x + y

R = reduce(sum,List)
print(R)