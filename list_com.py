# out=[i for i in range(1,11)]
# print(out)


# out=[i**2 for i in range(5,16)]
# print(out)




# out=[len(i) for i in [[1,2,3],'abcd',(1,2),{1,2,3},]]
# print(out)


# def fact(n):
#     out=1
#     for i in range(1,n+1):
#         out*=i 
#     return out
# out=[fact(i) for i in range(1,11) if i%2==0]
# print(out)

# import math
# out=[math.factorial(i) for i in range(1,11) if i%2==0]
# print(out)






# a=[9,'9',10,[1,3],'234',21,22.5]
# out=[(i,a[i]) for i in range(len(a)) if type(a[i])==int]
# print(out)



out=[i**2 if i%2==0 else i**3 for i in range(1,21)]
print(out)


