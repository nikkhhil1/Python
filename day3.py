#Dictionary
# info={
#     "key":"value",
#     "name":"nikhil",
#     "subjects":["python","C++"],
#     "topics":("set","tuple"),
#     "learning":"python",
#     "age":"20",
#     "marks":90
# }
# null_dict={}
# print(null_dict)
# info["name"]="Ritik"

# print(info)

#nested dictionary
# student={
#     "name":"nikhil",
#     "subjects ":{
#         "chem":98,
#         "phy":97,
#         "math":95
#     }
# }
# # print(list(student.keys()))
# # print(len(student))
# # print(list(student.values()))
# print(list(student.items()))
# print(student.get("name"))

# # student.update({"city":"delhi"})
# my_dict={"city":"delhi","age":20}
# student.update(my_dict)
# print(student)


#### set
# collection={1,2,3,4,4,"hello"}
# print(collection)
# collection=set() # empty set
# collection.add(1)
# collection.add(2)
# collection.add("nikhil")
# collection.add((1,2,3))
# # collection.remove(2)
# # collection.clear()
# # collection.pop()

# print(collection)
# set1={1,2,3,4}
# set2={3,4,5,6,}
# print(set1.union(set2)) 
# print(set1.intersection(set2))

#practice
#1
# d={"table":("a piece of furniture","list of facts and figures"),
#    "cat":"a small animal",}
# print(d)

#  2
# set={"python","java","c++","python",
#      "javascript","java","python","java","c++","c"}
# print(set)
# print(len(set))

#3
# d={}
# x=int(input("enter the phy:"))
# y=int(input("enter the math:"))
# z=int(input("enter the chem:"))
# d.update({"phy":x})
# d.update({"math":y})
# d.update({"chem":z})
# print(d)

##4
# values={9,"9.0"}
# print(values)
values={
    "int":9,
    "float":9.0
}
print(values )
 