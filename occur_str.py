str_o=input()
d={}
for k in str_o:
    if k in d:
        d[k]+=1
    else:
        d[k]=1
print(d)


st=input()
i=0
count=0 