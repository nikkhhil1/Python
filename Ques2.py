# Q1 find GCD/HCF
#  method 1
def hcf(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(hcf(48,18))

#  method2 using built in function
import math
print(math.gcd(48,18))

# multiple numbers HCF
import math
nums=[24,36,60]
result=nums[0]
for i in nums[1:]:
    result=math.gcd(result,i)
print(result)

#Q2 find LCM
# Method1 - using Euclid
import math
def lcm(a,b):
    return (a*b) // math.gcd(a,b)
print(lcm(12,18))

# method2 -- without built-in
def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//hcf(a,b)
print(lcm(12,18))

# method 3- multiple numbers LCM
import math
nums=[4,6,8]
result=nums[0]
for i in nums[1:]:
    result=(result*i)//math.gcd(result,i)
print(result)

# hvf=5 , product=100,  find lcm
hcf=5
product=100
lcm=product//hcf
print(lcm)


Q3 convert decimal to binary
n=int(input("enter number"))
binary=""
while n>0:
    remainder=n%2
    binary=str(remainder)+binary
    n=n//2
print("Binary=",binary)

# Method2 
def bin(n):
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n=n//2
    return binary
print(bin(5))
        
# Q3 count occurrence of character in string
def count_char(s,ch):
    count=0
    for i in s:
        if i==ch:
            count+=1
    return count
print(count_char("banana","a"))

# method 2
s="banana"
print(s.count("a"))

# Q4 count all characters
s="banana"
freq={}
for ch in s:
    if ch in freq:
     freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# method 2 - using dictionary
s='banana'
freq={ch: s.count(ch) for ch in s}
print(freq)

###
a="apple"
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# Q3  Remove duplicate from list
# method 1- using set
l=[1,1,2,3,4,5,21,4,5]
res=list(set(l))
print(res)

#  method 2 
l=[1,2,3,4,1,2,4,]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)

# method 3 using dictionary
l=[1,1,2,3,4,5,4,5]
res=list(dict.fromkeys(l))
print(res)

# Q4 remove duplicate from dtring'

def duplicate(s):
    res=""
    for i in s:
        if i not in res:
            res+=i
    return res
print(duplicate("banana"))

# method 2 using dict
s="banana"
res= "".join(dict.fromkeys(s))
print(s)

# Q5  Find second largest number
l=[23,44,56,6,7]
l.sort()
print(l[-2])

# Method 2 
l=[20,30,40,50]
largest=float('-inf')
second_larg=float('-inf')
for i in l:
    if i>largest:
        second=largest
    elif i>second and  i !=largest:
        second=i
print(second_larg)

# Q6  sort a list u
l=[4,3,2,1]
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
            
# method 2 
l=[3,4,5,3,1]
l.sort()
print(l)

# Q7 merge 2 list
l1=[1,2,3]
l2=[4,5,6]
res=[]
for i in l1:
    res.append(i)
for i in l2:
    res.append(i)
print(res)
