# n=input('enter any number from 0-6:-')
# match n:
#     case '0': print('sunday')
#     case '1': print('monday')
#     case '2': print('tuesday')
#     case '3': print('wednesday')
#     case '4': print('thursday')
#     case '5': print('friday')
#     case '6': print('saturday')
#     case _: print('enter valid input')

# a=int(input('enter a number:-'))
# b=int(input('enter b number:-'))
# n=input('enter any arithmetic operation:-')
# match n:
#     case '+': print('a+b',a+b)
#     case '-': print('a-b',a-b)
#     case '*': print('a*b',a*b)
#     case '/': print('a/b',a/b)
#     case '//': print('a//b',a//b)
#     case '%': print('a%b',a%b)
#     case '**': print('a**b',a**b)
#     case _: print('enter valid input')




n=int(input('enter a number:-'))
match n%2:
    case 0: print(n*n)
    case 1: print(n**3)
    case _: print('invalid input')