with open("C:\python start\pd\demo.txt","r")as f:
    data=f.read() 
    
    
# with open("C:\python start\pd\demo.txt","w") as f:
#     f.write("new data")
    

## Deleting a file
# import os
# os.remove("sample.txt")

# ## practice questions
# # Q1 create a new file " practice.txt" using python
# # add following data on it:
# # Hi everyone
# # we are learning File I/O
# # using python 
# # I like programming in python

# with open("practice1.txt","a") as f:
       

#     f.write("Hi everyone\n We are learning file I/O\n using python\n ")
#     f.write("I like programming in python")

# # Q2  replace occurrences of "python" with "java" in above file
# with open("practice1.txt","r") as f:
#     data=f.read()
# new_data=data.replace("python","java")
# print(new_data)
# # over write data
# with open("practice1.txt","w") as f:
#     f.write(new_data)


# # Q3 search if the word "learnig" exists in the file or not
# def check_for_word():
#     word="learning"
#     with open("practice1.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()


# # Q4 WAF to find in which line of the file does the word "learning" occur first
# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("C:\python start\practice1.txt","r")as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#             line_no+=1
#     return -1
# check_for_line()


# Q5 from a file containing numbers separated by comma,print the count of even numbers

count=0
with open("C:\python start\practice1.txt","r") as f:
    data=f.read()
    print(data)
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)
    

    