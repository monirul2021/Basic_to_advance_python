student1_name = "Sakib al hasan - eve"
student2_name = "Nannu"

# if student2_name.endswith("eve"):
#     student2_name = student2_name.replace("reg", "eve")
#     print("Student from evening batch")
#     # print("Hello")
#     # print("Hi")

# a = "", 0, None, False # falsy value
#  "hello", 23, 1.45, -3 # truthy value

# c = [1, 2, 3, 4]
# print(len(c))

# if len(c):
#     student2_name = student2_name.replace("reg", "eve")
#     print("Student from evening batch")
#     # print("Hello")
#     # print("Hi")

# print(student2_name)

# if student2_name.endswith("reg"):
#     print("Student from Regular batch")
    
#     # if student2_name.find("Nannu"):
#     if student2_name.startswith("Nannu"):
#         print("Helo Nannu")
#     else:
#         print("Sorry, Nannu. Better luck next time")

# else:
#     print("Student from Evening batch")

# if student2_name.endswith("reg"):
#     print("Student from Regular batch")
# elif student2_name.endswith("eve"):
#     print("Student from Evening batch")
# else:
#     print("Something went wrong. Please contact with admission section")

print("Student from regular batch") if student2_name.endswith("reg") else print("student from evening batch") if student2_name.endswith("eve") else print("Something went wrong. Please contact with admission secion")


print("Out of if block")