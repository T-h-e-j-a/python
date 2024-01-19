n=input('enter a string:-')
i=0
out=' '
while i<len(n):
    # if not('a'<=n[i]<='z' or 'A'<=n[i]<='Z' or '1'<=n[i]<='9'):
    if n[i]==' ':
        out+='_'
    else:
        out+=n[i]
    i+=1
print(out)

