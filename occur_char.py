n=input("enter string:")
char=input("enter character:")
i=0
count=0
while i<len(n):
    if n[i] in char :
        count+=1
    i+=1
print(count)