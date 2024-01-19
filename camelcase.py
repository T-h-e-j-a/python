n=input('enter a string:-')
i=0
out=' '
temp=True          #first character of the word
while i<len(n):
    if n[i]==' ':
        temp=True
    elif temp and 'a'<=n[i]<='z':
        out+=chr(ord(n[i])-32)
        temp=False
    else:
        out+=n[i]
        temp=False
    i+=1
print(out)

