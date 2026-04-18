#file open
f=open("C:\python start\pd\demo.txt","r")

## read file
data=f.read()
print(data)
print(type(data))

# read line wise
line1=f.readline()
print(line1)

## writing to the file
f1=open("C:\python start\pd\demo.txt","w")
f1.write("I want to learn javascript tomorrow. ")

## add data
f2=open("C:\python start\pd\demo.txt","a")
f2.write("\nAfter that nodejs")

## create new file
f=open("sample.txt","a")
f.close()