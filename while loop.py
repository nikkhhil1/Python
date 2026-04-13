## while loop

count=1
while count<=5:
    print("hello")
    count+=1

### print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
    
## 2 print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

## 3 print the multplication table of a number n
i=1
while i<=10: 
    print(3*i)
    i+=1

##4 

nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

##5 search for a number x in this tuple using loop

num=[1,4,9,16,25,36,49,64,81,100]
x=36
i=0
while i<len(num):
    if(num[i]==x):
        print("found",i)
        break
    else:
        print("finding...")
    i+=1
    
## break 
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

## continue
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
    
## questions
#Q1 find the sum of first natural numbers
n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)

#Q2 find the factorial of first n numbers
n=5
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print(fact)