n=input('enter string:-')
i=0
out=""
while i<len(n):
    if 'a'<=n[i]<='z':
        out+=chr(ord(n[i])-32)
    else:
        out+=n[i]
    i+=1
print(out)
