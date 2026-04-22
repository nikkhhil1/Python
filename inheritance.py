# single inheritance
class car:
    @staticmethod
    def start():
         print("car started.")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(car):   
    def __init__(self,name):
        self.name=name
car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.start())  


## Multilevel inheritance
class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car started")
class ToyotaCar(car):
    def __init__(self,brand):
        self.brand=brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("diesel")
car1.start()


## multiple inheritance
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class c"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)