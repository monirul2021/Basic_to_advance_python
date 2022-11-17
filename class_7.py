students = {
    "name" : "monirul",
    "age" : 23,
    "gender" : "male",    
}


#add item on students dict
students["cgpa"] = 3.14
#update valu on dict
students["age"] = 30


students.update({"skills" : "programming", "address" : "rajshahi" })
students.pop("address")
# students.popitem()
# print(students)
# # students.clear()
# print(students)
# # del students
# print(students)
students.setdefault("weight", 540)
print(students)

a = ("rahim", "karim", "jodu")
b = 100
boys = dict.fromkeys(a, b)
print(boys)


# for key in boys.keys():
#     print(key)

for val in boys.values():
    print(val)
    

for item in students.items():
    print(item[0], "=>", item[1])

name, age, marks = ("rahim", 34, 40)
print(name)



fro key, value in students.items():
print(key, "=>", Value)