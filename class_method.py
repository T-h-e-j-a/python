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
    def update_info(self,new):
        self.MOB=new
        self.SEM=new
        print('updated successfully')
    @classmethod
    def change_principal(cls,new):
        cls.principal=new
    
    def add(a,b):
        return a+b

        
stu1=mtca('theja',101,123456,'theja@gmail.com',1)
stu1.MOB=2341846
stu1.SEM=2
print(vars(stu1))
stu2=mtca('sree',102,345642,'sree@gmail.com',1)


print(mtca.principal)
print(stu1.principal)

stu1.change_principal('kutty')

print(stu1.principal)
print(stu2.principal)
print(mtca.principal)


