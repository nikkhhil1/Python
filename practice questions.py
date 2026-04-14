# Q1 accept numbers from the user
a=int(input("enter the number"))
print(a)

# Q2 
print("name", "is","james",sep="**")

# Q3 Display float numbers with two decimal places
a=45.45555
print(f"{a:.2f}")

#Q4 sum of two integers
a=3
b=4
sum=a+b
print(sum)

# Q5 accept 2 integer from the user and print the sum
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
sum=a+b
print(sum)

# Q6 Accept the User's name, age and print in following manner
#    Ex - Hello Shery, you are 12 years old.

name="Hello Shery"
age=12
print(f"{name}",f"you are {age} years old")

# Q7 Take 3 int inputs from user and check and print the result.
	# all are equal
	# any of two are equal
	# ( use and or )
a=2
b=3
c=2
if(a==b==c):
    print("all are equal")
elif(a==b or a==c or a==b):
    print("any 2 are equal")
else:
    print("all are diifferent")

# Q8  Accept two numbers and print the greatest between them
def number(a,b):
    if a>b:
        print("a is greater than b ")
    elif a<b:
        print("b is greater than a")
    else:
        print("both are equal")
        
number(2,3)

# Q9 Accept the gender from the user as char and print the respective greeting message
    #  Ex - Good Morning Sir (on the basis of gender)
a=input("enter the gender")
if(a=="male"):
    print("Good morning sir")
elif(a=="female"):
    print("Good morning mam")

# Q10 Extend the previous program and handle the wrong inputs.
    #   Print Good Morning sir for input m or M & Good morning Maam for input F or f 
    #   else print Wrong Input
a=input("enter the gender")
if(a=="male" or a=="Male"):
    print("Good morning sir")
elif(a=="female" or a=="Female"):
    print("Good morning mam")

# Q11 Accept an integer and check whether it is an even number or odd.
a=int(input("enter the number"))
if(a%2==0):
    print("number is even ")
else:
    print('number is odd')

#Q12 Accept name and age from the user. Check if the user is a valid voter or not.
#   case1  #   Vaid - Hello Shery, You are a valid voter.
#     #   Invalid - Sorry Shery, you can't cast the vote.
name=input("enter the number")
age=int(input("enter the age"))
if(age>=18 ):
    print(f"{name},you are a valid voter")
else:
    print(f"sorry {name} , you are not valid")
    
     #  case2  Print after how many years the user will be eligible

name=input("enter the number")
age=int(input("enter the age"))
eligible=18-age
if(age>=18 ):
    print(f"{name},you are a valid voter")
else:
    print(f"{name} you are eligibe after", f"{eligible} years" )


