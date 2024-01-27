# a=10
# def fun():
#     c=20
#     def inner():
#         c=40
#         print(a)
#         print(c)
#     print(c)
#     inner()
#     print(c)
# fun()


# a=10
# def fun():
#     c=20
#     def inner():
#         nonlocal c
#         c=40
#         print(c)
#     print(c)
#     inner()
#     print(c)
# fun()

def func(a,b,c,d=0,e=0):
    return a+b+c+d+e
print(func(a=1,c=2,b=3,d=4))