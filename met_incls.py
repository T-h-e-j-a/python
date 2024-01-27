class cname:
    a=10
    b=20
    def method(obj,x,y):
        obj.c=x
        obj.d=y
# obj=cname()
tej=cname()

# print(obj.a)

cname.method(tej,23,34)
print(tej.c)
