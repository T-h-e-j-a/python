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
stu1=mtca('theja',101,123456,'theja@gmail.com',1)
stu1.MOB=2341846
stu1.SEM=2
print(vars(stu1))


stu2=mtca('sree',102,345642,'sree@gmail.com',1)
print()





# print(vars(stu2))

                                    #   to get the values int the form of dictionar

# print(stu2.__dict__)              



