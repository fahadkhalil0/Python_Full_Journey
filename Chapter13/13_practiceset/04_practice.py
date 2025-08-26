# practice task no 04

def divisible5(n):
    if (n%5 == 0):
        return True
    return False

l = [2,4,5,6,7,8,9,00,12,123,1678,5555]
filter = filter(divisible5, l)
print(list(filter))