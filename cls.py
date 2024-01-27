class cname:
    a=10
    b=20
obj=cname()
obj1=cname()
print(obj.a)
print(obj1.a)
print(cname.a)

obj.a=50
print(obj.a)     #a=50
print(obj1.a)    #a=10
print(cname.a)   #a=10



obj.c=30
obj.d=40

print(obj.c)               #30




obj1.c=50
obj1.d=60

print(obj1.c)            #50


