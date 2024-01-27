# def odd(n):
#     for i in range(len(n)):
#         if i%2==1 and n[i]%2==1:
#             print(i**2+n[i]**2)
#         elif i%2==0 and n[i]%2==0:
#             print(i**2+n[i]**2)
#         elif i%2==1 and n[i]%2==0:
#             print(i+n[i])
#         else:
#             print(i+n[i])
#     return ((i**2+n[i]**2),(i**2+n[i]**2),(i+n[i]),(i+n[i]))
# print(odd([2,4,9,7,11,2,4,3,5,7,6]))



def even(value):
    flag=False
    if value%2==0:
        flag=True
    return flag
def squAdd(a,b):
    return a**2+b**2
def add(a,b):
    return a+b
def index_value(arr):
    out=[]
    for i in range(len(arr)):
        if not(even(i) ^ even(arr[i])):
            out+=[squAdd(i,arr[i])]
        else:
            out+=[add(i,arr[i])]
    return out
print(index_value([2,4,9,7,11,2,4,3,5,7,6]))
    


