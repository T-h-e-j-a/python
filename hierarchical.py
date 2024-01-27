class Mtca:
    chairman='mr.sunil'
    location='palamaner'
    college='MTCA'

    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mca(Mtca):
    principal='mr.prabhakar'
    strength=240
    staff=9
class Btech(Mtca):
    principal='ms theja'
    strength=300
    staff=30

thej=Mca('sree',1234567898)
sri=Btech('chandu',987654321)

# thej=Mtca()
print(thej.principal)
print(sri.staff)
print(thej.chairman)

print(vars(thej))
print(vars(sri))
