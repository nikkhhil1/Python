## functions

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(2,3)
calc_sum(12,7)

##
#function definition
def cal(a,b):# parameters
    return a+b
sum=cal(3464,4) #function call; arguments
print(sum)

##
def print_hello():
    print("hello")
print_hello()
print_hello()

##
# average of 3 numbers
def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
average(21,34,55)

##
print("nikhil",end=" ") # sep=" "
print("sharma")

# default parameter
def cal_prod(a=1,b=1):
    print(a*b)
    return a*b
cal_prod()

#practice questions
# Q1 print the length of the list
cities=["delhi","noida","pune","mumbai"]
heros=["thor","ironman","captain america"]
def lst(list):
    print(len(list))
    
lst(cities)
lst(heros)

# Q2 print the elements of a list in a single line
def print_lst(list):
    for item in list:
        print(item,end=" ")
        
print_lst(heros)
print(  )

# Q3 find the factorial of n
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    
factorial(5)

# Q4 convert USD to INR
def convertor(usd):
    inr_value=usd*92
    print(usd,"USD=",inr_value, "INR")
    
convertor(2)

# Q5 
def number(n=int(input("enter the number"))):
    if n%2==0:
        print("even")
    else:
        print("odd")
number()
