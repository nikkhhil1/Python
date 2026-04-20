# object oriented programming
#class
class student:
    name="karan"
#object
s1=student()
print(s1.name)
s2=student()
print(s2.name)

class Car:
    color="blue"
    brand="mercedes"
car1=Car()
print(car1.color)

# __init__ function()   ,,(constructor)
class student:
    name="karan"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in Database..")
s1=student("karan",97)
print(s1.name,s1.marks)
s2=student("arjun",77)
print(s2.name,s2.marks)

class student:
# default constructor
    def __init__(self):
        pass
    
    # parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in Database")
s1=student("karan",77)
print(s1.name,s1.marks)
s2=student("arjun",99)
print(s2.name,s2.marks)    


# class & instance attributes
class student:
    college_name="ABC college"
    name="anonymous" # class str
    
    def __init__(self,name,marks):
       self.name=name# obj attr > class attr
       self.marks=marks
       print("adding new student in database")
s1=student("karan",97)
print(s1.name)

# Methods
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def hello(self):
        print("hello", self.name)
    def get_marks(self):
        return self.marks
        
s1=student("nikhil",97)
s1.hello()
print(s1.get_marks())


# practice question
# Q1
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your avg score is:",sum/3)
        
s1=student("tony stark",[78,98,88])
s1.get_avg()
s1.name="tony"
s1.get_avg()

# static methods
class student:
    @staticmethod
    def college():
        print("ABC college")
    college()


# Abstraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")
car1=Car()
car1.start()

# Encapsulation
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")
car1=Car()
car1.start()

# practice question
# Q1 create account class with 2 attributes -balance & account NO,
# create methods for dabit,credit&printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount, "was debited")
        print("total balance=",self.get_balance())
        
    def credit(self,amount):
        self.balance+=amount
        print("Rs,", amount, "was credited")
        print("total balance=",self.get_balance())
        
    def get_balance(self):
        return self.balance
        
        
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(500)
acc1.credit(200)
acc1.debit(7000)
acc1.credit(100000)

