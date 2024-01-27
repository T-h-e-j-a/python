from abc import ABC,abstractmethod
class modelcar(ABC):
    @abstractmethod
    def Break():
        pass
    @abstractmethod
    def speed_up():
        pass 
    @abstractmethod
    def speed_down():
        pass

class nexon(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    def speed_up(self):
        self.speed+=5
        self.stop=False
        print(f'accelerated by 5 km/hr and current speed is {self.speed}')
    def Break(self):
        self.speed=0
        self.stop=True
    def speed_down(self):
        if not self.stop:
            self.speed-=5
            if self.speed==0:
                self.stop=True
        print(f'deaccelerated by 5 km/hr and current speed is {self.speed}')

class indica(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    def speed_up(self):
        self.speed+=10
        self.stop=False
        print(f'accelerated by 5 km/hr and current speed is {self.speed}')
    def Break(self):
        self.speed=0
        self.stop=True
    def speed_down(self):
        if not self.stop:
            self.speed-=5
            if self.speed==0:
                self.stop=True
        print(f'deaccelerated by 5 km/hr and current speed is {self.speed}')

obj=nexon()
obj1=indica()


print(obj.speed_up())
print(obj.speed_up())
print(obj.speed_down())
print(obj.Break())



