## for loop

list=[1,2,3,4,5]
for i in list:
    print(i)
    
##
tup=(1,2,3,4,5)
for num in tup:
    print(num)
    
## 
str="nikhilsharma"
for i in str:
    print(i)
else:
    print("end")
    
##
str="nikhilsharma"
for i in str:
    if(i=="s"):
        print("s found" )
        break
print("end")

##Q 1 search for a element x in this tuple     
n=(1,2,3,4,5)
x=3
idx=0
for i in n:
    if(i==x):
        print("found at idx",idx)
        break
    idx+=1


## Q2 print the element of the following list using a loop
lst=[1,4,9,16,25,36,49,64,81,100]
for i in lst:
    print(i)
    
#### range
for i in range(10): # range stop
    print(i)
    
for i in range(2,10): # range(start,stop)
    print(i)

for i in range(2,10,2):
    print(i)
    
### print even numbers
for i in range(2,100,2):
    print(i)
    
## print odd numbers
for i in range(1,100,2):
    print(i)
    
## practice 
# Q1
for i in range(1,100+1):
    print(i)
    
#Q2
for i in range(100,1,-1):
    print(i)
    
#Q3 print the multiplication table of n
n=int(input("enter the number"))
for i in range(1,11,):
    print(i*n)
    
## pass statement
for i in range(5):
    pass
print("some useful work")


###     practice question
#Q1 find the sum of first natural numbers
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("Total sum=",sum)

 
n=4
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
    
