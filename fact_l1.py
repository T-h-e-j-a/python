res=[]
a=[2,4,7,3,5]
for b in a:
    out=1
    for k in range(1,b+1):
        out*=k
    res=[out]
    print(res)