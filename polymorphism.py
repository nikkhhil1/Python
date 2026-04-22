# polymorphism : operator overloading

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
        
    def __add__(self,num2): # By the dunder function
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