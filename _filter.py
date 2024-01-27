# a=[1,0,True,'','str',[1,2,3],78,0.0]
# # out=[a[i] for i in range(len(a)) if bool(a[i])==True]
# out=[i for i in a if bool(i)]
# print(out)

#using filter


# b=filter(bool,a)
# print(list(b))




                    
a=[2,57,8,6,4,3,23,2,1,21,35,8,9]

def mult3(n):
    if n%3==0:
        return True
    else:
        return False
b=list(filter(mult3,a))
print(b)



#using lambda
print(list(filter(lambda n:n%3==0,a)))