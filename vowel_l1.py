# n=input('enter string')
# i=0
# out=[]
# while i<len(n):
#     if n[i] in 'aeiouAEIOU':
#         out+=[i]
#     i+=1
# print(out)


n=input('enter string')
out=[]
for i in range(len(n)):
    if n[i] in 'aeiouAEIOU':
        out+=[i]
print(out)