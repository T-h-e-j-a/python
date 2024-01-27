
from functools import reduce
b=[1,2,3,4,5]
c=reduce(lambda x,y,:x+y,map(lambda b:b**2,b))
print(c)