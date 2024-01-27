# def ran(a,b,c):
#     for i in range(a,b,c):
#         print(i,end=" ")
# ran(1,10,2)
# print()
# ran(1,100,3)


def ran(start,stop,step):
    out=[]
    while start<stop:
        out+=[start]
        start+=step
    print(out)
ran(1,15,2)