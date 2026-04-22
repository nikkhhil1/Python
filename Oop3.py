
# property decorater
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    # def calcPercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage)

# Polymorphism : operator overloading
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
        
    def __add__(self,num2):  ## By thr dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
num1=Complex(1,5)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

# num3=num1.Add(num2)
num3=num1+num2
num3.showNumber()