# list
# marks=[94.4,87.5,92,2,96.7,45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks)) 

# student=["karan",95.4,17,"delhi"]
# print(student)
# student[0]="arjun"
# print(student)

# marks=[12,3,4,5,56,55]
# print(marks[1:4])

# methods is list
# l=[1,2,3]
# l.append(4)
# print(l) 
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# l.insert(1,5)
# print(l)

## Tuples
# tup=(1,2,3,4)
# print(tup)
# print(tup[1:3])

# practice
#1
# l=input("enter the first movie")
# l2=input("enter the second movie")
# l3=input("enter the third movie")
# print([l,l2,l3])
# or append se bhi kr skte hai

#2
l=[1,2,1]
l2=[1,2,3]
copy_l=l.copy()
copy_l.reverse()

if(copy_l==l):
    print("palindrome")
else:
    print("not pallindrome")
    
#3
tup=["C","D","A","A","B","B","A"]
tup.sort()
print(tup)

print(tup.count("A"))
