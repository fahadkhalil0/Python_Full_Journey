#Practice task no 03

# convert a list into a vertical string 
# table = []

# n = 5
# for i in range(1,11):
#     n = f"{n} x {i} = {n*i}" 
#     table.append(n)

# print(table)

table = [str(7*i) for i in range(1,11)]

join = "\n".join(table)

print(join)