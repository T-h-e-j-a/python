# st=input()
# i=0
# while i<len(st):
#     if st[i] not in st[i+1:]:
#         print(st[i])
#         break
#     i+=1


st=input()
i=-1
while i>=-len(st):
    if st[i] not in st[:i-1]:
        print(st[i])
        break
    i-=1