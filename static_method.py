class mtca:
    principal='mr.prabhakar naidu'
    college='mtca'
    location='palamaner'
    def __init__(self,stuname,id,mobile,email,sem):
        self.SNAME=stuname
        self.ID=id
        self.MOB=mobile
        self.EMAIL=email
        self.SEM=sem 
    @staticmethod 
    def add(a,b):
        return a+b

        
stu1=mtca('theja',101,123456,'theja@gmail.com',1)


stu2=mtca('sree',102,345642,'sree@gmail.com',1)

print(stu1.add(2,3))



