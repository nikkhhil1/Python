class student:
    def __init__(self,name):
        self.name=name
s1=student("Nikhil")
print(s1.name)
del s1.name
print(s1.name)

#private attributes and methods
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass   )
     
acc1=Account("12345","abcde ")
print(acc1.acc_no)
print(acc1.reset_pass)


class Person:
    __name="anonymous"
    
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()
p1=Person()
print(p1.welcome)

# inheritance
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

# multilevel inheritance
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
        
#Multiple inheritance

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


# super method
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        self.name=name
        super().start()
car1=ToyotaCar("prius","electric")
print(car1.type)


#class method
class Person:
    name="anonymous"
    
    # def changeName(self,name):
    #     # self.name=name
    #     # Person.name=name
    #     self.__class__.name="rahul"
    
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

