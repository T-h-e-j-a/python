# for k in [1,2,3,4]:
#     print(k)



n='user@123#admin'
out=''
for i in n:
    if  not '0'<=i<='9':
        out+=i
print(out)
