class A:
    a=10
class B:
    b=20
class B1(B):
    pass
class C(A):
    c=30
class D(C,B):
    d=40
print(C.c)