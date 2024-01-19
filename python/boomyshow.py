print(' \n 1-->Diamond \n 2-->Gold \n 3-->silver')

c=eval(input("choose category:"))
if c==1:
    d=200
    print("The cost is 200rs")
elif c==2:
    d=150
    print("The cost is 150rs")
elif c==3:
    d=100
    print("The cost is 100rs")
    

else:
    print("select any one in the above list")

print('seats : \n 1-->adult \n 2-->children')
a=int(input("no.of adults:"))
b=int(input("no.of childs:"))
print("total no.of seats are: ",a+b)

print("\n 1-->Ac \n 2-->non-Ac")

ac=int(input("enter choice:"))
if ac==1:
    print("amount for adults",10*a*d)
    print("amount for childrens",5*b*d)
    print("the total amount is:",(10*a*d)+(5*b*d))
    print("bon voyage.....!")
elif ac==2:
    print("amount for adults",5*a*d)
    print("amount for childrens",3*b*d)
    print("the total amount is:",(5*a*d)+(3*b*d))
    print("bon voyage.....!")

print("press 'yes' if u confirm the tickets")
s=input()
if s=="yes":
    print("conform ur tickets")
else:
    print("get lost")