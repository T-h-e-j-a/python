class num:

    def __init__(self,a):
        self.a=a
    def __str__(self):
        return str(self.a)
    def square(self):
        return self.a**2
    def cube(self):
        return self.a**2
    def double(self):
        return self.a*2
    def even(self):
        if self.a%2==0:
            return True
        else:
            return false

    def prime(self):
        flag=True
        if self.a>1:
            for val in range(2,self.a):
                if self.a%val==0:
                    flag=False
                    break
        return flag
    def factorial(self):
        out=1
        if self.a>1:
            for val in range(1,self.a+1):
                out*=val
            return out
    def increment(self,step=1):
        self.a=self.a+step
        return self.a
    def decrement(self,step=1):
        self.a=self.a-step
        return self.a
obj=num(3)
print(obj.prime())
print(obj.factorial())
