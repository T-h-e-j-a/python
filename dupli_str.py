# n = input()
# l1=[]
# for i in n:
#   if n.count(i)>1 and i not in l1:
#     l1+=i
# print(l1)




# str=input()
a='hello world'
out=''
for i in range(len(a)):
    # if i!=len(a)-1 and a[i] in a[i+1:]:
    if  a[i] in a[i+1:]:
        if a[i] not in out:
            out+=a[i]
print(out)