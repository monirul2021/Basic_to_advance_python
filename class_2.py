# introduction to python data types
    # - str
        # 'hello', "rahim", "I go to school"

    # - int, float, complex
        # example of int: 1,10, 100, 33
        # example of float: 1.5, 10.3, 88.88333
        # example of complex: 10j, 77j

    # - list, tuple, range
        # info = ["rahim", 5, 3.9, [5, 6, "korim"]]
        #         # 0, 1, 2, 3

        # print(info[3][2])

        # print(info[3][2])

        # info1 = ("rahim", 5, 3.9, ["3", "korim", 9.9])

        # range(10) # here we've defined the ending position of a range
        # range(5, 10) # here we've defined starting position by giving 1st parameter and defined ending position by giving the 2nd parameter
        # range(1, 20, 2) # here the 1st parameter is the starting position, 2nd parameter is the ending position and the third parameter is the step

    # - dict
        # person = {"name": "Rahim", "age": 34, "height": 5.5, "childs": [{"name": "Rafiq", "age": 13, "height": 4.5}, {"name": "Sofiq"}]}

        # person["age"] = 55

        # print(person["age"])
        # print(type(person))

    # - set, frozenset
        # students = {"Rahim", "Karim", "Noman", "Hasib", "Rahim", "Rahim", "Noman"}
        # print(students[0])
        # print("Abdul" in students)
        # frozenset((1, 3, 5, 8, 8, 5))

    # - bool
            # students = [{"name": "Rahim", "age": 13, ""gender": "Male""}, {"name": "Rahima", "age": 15, "gender": "Female"}]
            # True, False
            # is_male = True

    # - bytes, bytearray, memoryview

    # - None
    # number_of_packets = 5
    # number_of_packets = None
    # print(type(number_of_packets))

# operators in python
    # - Arithmetic operators
        # +, -, *, /, %, **, //
        # PEMDAS
        # P = PARENTHESIS ()
        # E = EXPONENT **
        # M = MULTIPLICATION *
        # D = DIVISION /
        # A = ADDITION +
        # S = SUBTRACTION
        # print((5 + (4 - 9)) / 2 * 6)

    # - Assignment operators
        # =, +=, -=, /=, %=, //=, **=

        # name = "Rahim"

        # age = 15

        # age = age + 3

        # age += 3

    # - Comparison operators
        # ==, !=, >, <, >=, <=
        # print(3 >= 3)

    # - Logical operators
        # and, or, not

        # if rahims_age > karims_age and rahims_age > abduls_age:
        #     print("Rahim is the elder brother")

        # if new_comer == "teacher" or new_comer == "student":
        #     print("You're welcome")

        # if new_comer == "teacher" not new_comer == "student":
        #     print("Sorry, you're not welcome")

    # - Identity operators
        # is, is not

        # print(3 is 3)

    # - Membership operators
        # in, not in

        # students = ["Rahim", "Karim", "Sajal"]

        # print("Abdul" in students)
        
    # - Bitwise operators

# operator precendence in Python

# input
    # name = input("What's your name? :")
    # print("Hi " + name + ". How are you?")

# output
    # print("HELLO","World","HI", sep="-")

    # print("Hi there", end="*")
    # print("How are you")

# variables
    # sum_of_numbers = 3 + 4 + 6

    #     # pascal case = StudentOneName

    #     # camel case = studentOneName

    #     # snake case = student_one_name # used for declaring variables

    # print(sum_of_numbers)

# comments
    #I am a student
    #jksdfjdsklfjdsfkldsfjsdf