# l1=[1,2,3,4,5,6]
# if len(l1)>5:
#     print("collection is greater than 5")




# a=[10,20,3,40]
# if 3 in a:
#     print("yes")

# b=(1,2,3,4,5)
# if 3 in b:
#     print("yes")

# c={1,2,3,4}
# if 3 in c:
#     print("yes")


# n=int(input("enter any number:"))
# if n%2==0:
#     print(n," is even")
# else:
#     print(n," is odd")



# n=input("enter any digit:")
# if n in "0123456789":
#     print("it is digit")
# else:
#     print("it is not digit")

        #or

# n=input("enter any digit:")
# # if '0<=n' and '9'>=n:
# if '0'<=n<='9':
#     print("it is digit")
# else:
#     print("it is not digit")


# n=input("enter any value:")
# if 'A'<=n<='Z':
#     print("it is in uppercase")
# else:
#     print("it is not in uppercase")


# n=input("enter any value:")
# if n in 'aeiouAEIOU':
#     print("it is vowel")
# else:
#     print("it is not vowel")


# n=eval(input())
# if len(n)%2==0:
#     print(n[0],n[-1])
# else:
#     print(n[len(n)//2])


# n=eval(input("enter any value:"))
# if type(n) in (bool,int,float,complex):
#     print(n**2)
# else:
#     print(3*len(n)+1)

# print(ord('4'))




# n=input("enter any value: ")
# if '0'<=n<='9':
#     print("it is number")
# elif 'a'<=n<='z':
#     print("it is lowercase")
# elif 'A'<=n<='Z':
#     print("it is uppercase")
# else:
#     print("it is special character")


# # n=input("enter any value: ")
# # if n in "0123456789":
# #     print("it is number")
# # elif a>='a':
# #     print("it is lowercase")
# # elif 'A'<=n<='Z':
# #     print("it is uppercase")
# # else:
# #     print("it is special character")   

# incomplete



# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# if a>b and a>c:
#     print("a is big")
# elif b>c and b>a:                #elif b>c:
#     print('b is big')
# else:
#     print("c is big")




# db={'username':"thejasree",'password':'12345'}
# username=input("username: ")
# password=input("password: ")
# if username == db['username'] and password==db['password']:
#         print("username and password is",username,password)
# else:
#         print("invalid username and password")



# a=int(input("a:"))
# b=int(input("b:"))
# c=input("enter symbol: ")
# if c=='+':
#         print(a+b)
# elif c=='-':
#         print(a-b)
# elif c=='*':
#         print(a*b)
# elif c=='/':
#         print(a/b)
# elif c=='%':
#         print(a%b)
# elif c=='//':
#         print(a//b)
# elif c=='**':
#         print(a**b)
# else:
#         print("invalid arithmeric operator")


# a=int(input("a:"))
# b=int(input("b:"))
# c=input("+,-,*,%,/,//,** :")
# match c:
#         case '+':print(a+b)
#         case '-':print(a-b)
#         case '*':print(a*b)
#         case '/':print(a/b)
#         case '//':print(a//b)
#         case '%':print(a%b)
#         case '**':print(a**b)
#         case _:print("invalid")


# a=input("player1: ")
# b=input("player2: ")
# if a=='rock' and b=='paper':
#         print("player 2 win")
# elif a=='paper' and b=='scissors':
#         print("player2 win")
# elif a=='rock' and b=="scissors":
#         print("player 1 win")
# elif a=='scissors' and b=='paper':
#         print("player1 is win")
# elif a=='scissors' and b=='rock':
#         print("player2 win")
# elif a=="paper" and b=='rock':
#         print("player 1 win")
# elif a==b:
#         print("both are tie")

# else:
#         print("invalid inputs")

                        #or
                        
# print('enter \n 1--->ROCK \n 2--->PAPER \n 3---> scissors')
# p1=input('player1:- ')
# p2=input('player2:- ')

# if p1==p2:
#         print("match tie")
# elif p1 == '1' and p2 == '3':
#         print('player1 won')
# elif p1 == '2' and p2 == '1':
#         print('player1 won')
# elif p1 == '3' and p2 == '2':
#         print('player1 won')
# else:
#         print("player2 won")



                                #2nd maximum number

# a=int(input('enter a number:-'))
# b=int(input('enter a number:-'))
# c=int(input('enter a number:-'))

# if a==b==c:
#         print("same")
# elif a>b and a>c:
#         if b>c:
#                 print(b,'is the greatest number')
#         else:
#                 print(c,'is the greatest number')
# elif b>c:
#         if a>c:
#                 print(a,'is the greatest number')
#         else:
#                 print(c,'is the greatest number')
# else:
#         if a>b:
#                 print(a,'is the greatest number')
#         else:
#                 print(b,'is the greatest number')


marks=eval(input("enter student marks:"))
if marks>90 and marks<=100:
        print("A+")
elif marks>80 and marks<=90:
        print("A")
elif marks>70 and marks<=80:
        print("B+")
elif marks>60 and marks<=70:
        print("B")
elif marks>50 and marks<=60:
        print("c")
elif marks>=35 and marks<=50:
        print("pass")
elif marks>0 and marks<35 :
        print("fail")
else: print("invalid marks")
