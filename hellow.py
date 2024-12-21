# print("hellow world!")
# output: hellow world!


# name = "Ayan"
# age = 19
# is_developer = True


# print(name,age,is_developer)
# output:Ayan 19 True


# name = input("Enter your Name")
# age = input("Enter your Age")

# print(age, name)

# name = input("Enter your Name")
# age = input("Enter your Age")

# print(f"My name is {name} and my age is {age}")
# My name is Ayan and my age is 19

# num1 = int(input("Enter your num 1"))
# num2 = int(input("Enter your num 2"))

# sum = num1 + num2

# print(sum)
# Enter your num 119
# Enter your num 220
# 39

# if False :
#     print("Ayan")
# else:
#         print("False")

# fruits = ["apple", "banana", "cherry"]

# for f in fruits:
#     print(f)

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# for num in range(10):
#     if num == 5:
#         break
#     print(num)

# for num in range(10):
#     if num == 5:
#         continue
#     print(num)

#Fractional 

# number = int(input("Enter a number: "))
# factorial = 1

# while number > 0:
#     factorial *= number  # factorial = factorial * number
#     number -= 1          # number ko kam karte rahenge

# print("Factorial is:", factorial)



# Functions 

# def hellow_world():
#     return"Hellow World"


# print(hellow_world()) #Hellow World

# def greet_user(name):
#     print(f"Hello, {name}!")

# greet_user("Ayan")   # Output : Hello, Ayan

# def greet_user(name):
#     print(f"Hello, {name}!")

# greet_user(input("Enter your Name ")) # Output : Hello, {your name}

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print("Sum:", result)  #output :  Sum: 8


# def factorail(num):
#     result = 1
#     while num > 0 :
#         result *= num
#         num -= 1    
#     return result

# print(factorail(3))


# List / In JavaScript Array


my_list = [1, 2, 3, 4, 5]  # Integers ka list
fruits = ["apple", "banana", "cherry"]  # Strings ka list
mixed = [1, "apple", True, 3.14]  # Mixed data types

# fruits[1] = "blueberry"

# print(fruits)

# fruits.append("orange")

# print(fruits)

# fruits.insert(1, "mango")
# print(fruits)

# fruits.remove("mango")
# print(fruits)


# fruits.pop()
# print(fruits)


# for fruit in fruits:
#     print(fruit)

# print(len(fruits))


# numbers = [10, 20, 30, 40, 50]

# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

# names = []
# for _ in range(3):
#     name = input("Enter a name: ")
#     names.append(name)
# print("Names:", names)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# evens = [num for num in numbers  if num % 2 == 0 ]
# odds = [num for num in numbers  if num % 2 != 0 ]

# print("Even numbers:", evens)
# print("Odd numbers:", odds)

my_dict = {"key1": "value1", "key2": "value2"}
student = {
    "name": "Ayan",
    "age": 19,
    "skills": ["Python", "React"]
}

# print(student["name"])  # Output: Ayan
# print(student.get("age"))

# student["city"] = "Mumbai"  # Add
# student["age"] = 26  # Update
# print(student)

# student.pop("city")
# print(student)

# for key, value in student.items():
#     print(key, ":", value)


# print("name" in student)  # Output: True
# print("gender" in student)  # Output: False

# dictionary = {}

# for _ in range(3):
#     word = input("Enter Word")
#     meaning = input(f'Enter {word} meaning')
#     dictionary[word] = meaning

# print(dictionary)


my_dict = {"a": 1, "b": 2, "c": 3}
keys = list(my_dict.keys())
values = list(my_dict.values())
print("Keys:", keys)
print("Values:", values)

    