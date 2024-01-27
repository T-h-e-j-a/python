# n=int(input())
# m=int(input())
# for i in range(n):
#     for j in range(m):

#         print("+" ,end=" ")
#     print()


    #or

# rows=int(input('enter a number'))
# for _ in range(rows):
#     print('* '*rows)


# n=int(input())
# out=''
# for i in range(n):
#     for j in range(n):
#         if i==j or i==n-j-1:

#             out+='  '
#         else:

#             out+='* '
#     out+='\n'
# name=input('enter file name:-')
# with open(f'{name}.txt','w') as file:
#     file.write(out)



# n=int(input())
# out=''
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:

#             out+='  '
#         else:

#             out+='* '
#     out+='\n'
# print(out)



# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0  or i==n-1 or j==n-1 or i==n//2 or j==n//2 or i+j==n-1 or i==j:
#             print("*",end=" ")
#         else: print(" ",end=" ")
#     print()


# n=int(input())
# for i in range(n):
#     val=1
#     for j in range(n+i):
#         if i+j>=n-1:
#             print(val,end=" ")
#             val=val+1 if j<n-1 else val-1
#             if val>9: val=1
#             if val<1: val=9
#         else: print(" ",end=" ")
#     print()


a=input()
i=0
while i<len(a) and '*' in a:
    if a[i]=='*':
        a=a[:i-1]+a[i+1:]
        i-=1
        continue
    i+=1
print(a)