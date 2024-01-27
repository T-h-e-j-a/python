b=[2,8,6,4,3,23,2,1,8,9]
# print(list(map(lambda b:b*b,b)))


# b=[2,8,6,4,3,23,2,1,8,9]
# def mult3(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# c=list(filter(mult3,b))
# print(c)
# print(list(map(lambda k:k**3,filter(mult3,b))))

#or

# print(list(map(lambda k:k**3,(filter(lambda b:b%2==0,b)))))



def length(n):
    if type(n)!=int:             #(or) if type(n) in [str,tuple,list,set,dict]
        return len(n)
    else:
        return n
b=[1,2,[4,5,6],'xyz',(4,1,2,3)]
c=list(map(length,b))
print(c)