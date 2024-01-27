# def fun(a,b):
#     yield a+b
#     yield a*b
# out=fun(3,2)
# print(list(out))



# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b  
# out=fib(10)
# print(list(out))


# def func(n):
#     a=b=1
#     for i in range(n):
#         a=b
#         yield a
#         b=a+b
# out=func(10)
# print(list(out))



def binary(n):
    while n>0:
        yield n%2
        n=n//2
out=''
for i in binary(10):
    out=str(i)+out
print(out)

