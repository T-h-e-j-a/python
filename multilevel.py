class parent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d

class child(parent):
    a=30
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f

class child2(child):
    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h


obj=child2(4,5,6,7,2,1)

# obj=parent(2,3)
print(obj.__dict__)