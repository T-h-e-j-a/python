class cname:
    __a=20
    b=30
    def __init__(self,c,d):
        self.__c=c 
        self.d=d 
    def __display(self):
        print(self.__c,self.d)
    @classmethod
    def classdisplay(cls):
        print(cls.__a,cls.b)
obj=cname(3,4)