n='hello world'
out=''
for i in n:
    if i in out:
        out+=''
    else:
        out+=i
print(out)


a='good'
out=''
for i in a:
    if i not in out:
        out+=i
print(out)


b=[1,2,3,4,3,2,4,5,7,6,8]
print(list(set(b)))

print(2.4%2)