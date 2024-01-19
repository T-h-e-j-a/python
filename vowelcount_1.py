n=input("enter string:-")
i=-1
count=0
while i>=-len(n):
    if n[i] in 'aeiouAEIOU':
        count+=1
    i-=1
print(count)