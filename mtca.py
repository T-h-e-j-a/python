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
stu1=mtca('theja',101,123456,'theja@gmail.com',1)
print()
print(mtca.principal)
print(mtca.college)
print(mtca.location)
print()

print('students present in mtca college')
print()
print('name:',stu1.SNAME)
print('id:',stu1.ID)
print('mobile:',stu1.MOB)
print('email:',stu1.EMAIL)
print('sem:',stu1.SEM)
print()
stu2=mtca('sree',102,345642,'sree@gmail.com',1)
print()
# print('name:',stu2.SNAME)
# print('id:',stu2.ID)
# print('mobile:',stu2.MOB)
# print('email:',stu2.EMAIL)
# print('sem:',stu2.SEM)




# print(vars(stu2))

                                    #   to get the values int the form of dictionar

# print(stu2.__dict__)              



