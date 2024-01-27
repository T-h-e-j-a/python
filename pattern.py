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



n=int(input())
out=''
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:

            out+='  '
        else:

            out+='* '
    out+='\n'
print(out)