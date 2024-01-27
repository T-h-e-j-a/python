class Add:
    @staticmethod
    def add2(a,b):
        return a+b
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class Sub:
    @staticmethod
    def sub2(a,b):
        return a-b
class Mul:
    @staticmethod
    def mul2(a,b):
        return a*b
class Cal(Add,Sub,Mul):
    pass

obj=Cal()
print(obj.add2(3,4))
print(obj.add3(7,4,1))
print(obj.sub2(9,6))
print(obj.mul2(2,7))


