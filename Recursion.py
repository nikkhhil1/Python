## recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(3)

## Factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(5))

## practice question
# Q1 write a recursion function calculate the sum of first natural numbers

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
print(calc_sum(5))
    
# Q2 wrire a recursive function to print all elements in a list... 
# Hint.. use list and index as parameters

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","banana","apple"]
print_list(fruits)
