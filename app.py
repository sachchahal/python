# print("Hi Sachin")

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# Falsy


# primitiveve type.. strings, boolean, variables

# x = 10 % 3
# print(x)

# temp = 12
# if temp > 20:
#     print("pleasent")
#     print("drink beer")
# elif temp < 20:
#     print("drink scotch")
# print("finish")


# ternary operator
# logical operators
# AND OR NOT

# high_income = True
# good_credit = True
# if high_income and good_credit:
#   print("eligible")
# else:
#    print("not eligible")


# short-circut evaluation.. logical operators are short citcut.
# high_income = True
# good_credit = True
# if high_income and good_credit:
#     print("eligible")
# else:
#     print("not eligible")


# Chaining Comparision Operators
# age = 33
# if 18 <= age < 65:
#     print("still young")


# For Loop

# for number in range(3):
#   print("send a message", number + 1, (number + 1) * ".")

# for number in range(1, 4):
#   print("attempt to send a message", number, number * ".")

# for number in range(1, 10, 2):
#   print("Attempt to send", number, number * ".")

# sucessful = True
# for number in range(3):
#   print("Attempt")
#  if sucessful:
#     print("success")
#    break

# else:
#   print("tried three times and failed")


# for x in range(5):
#   for y in range(3):
#      print(f"({x}, {y})")


# print(type(5))

# print(type(range(5)))

# range is iteable
# for x in "Python":
#   print(x)

# While Loop
# number = 100
# while number > 0:
#    print(number)
# or number = number // 2
#    number //= 2


# command = ""
# while command.lower() != "quit":
#   command = input("#:")
#  print("ECHO", command)


# while True:
#   command = input(">")
#  print("ECHO", command)
# if command.lower() == "quit":
#    break

# count = 0
# for number in range(1, 10):
#   if number % 2 == 0:
#      count += 1
#     print(number)
# print(f"we have {count} even numbers")


# Writing a function.
# #in brackets of the function where defining it we can call it PRARAMETERS - An input variable for the function.
# Argument - A value that is passed for the parameters.


# def greet(first_name):
#     print(f"hi {first_name}")
#     print("welcome")


# greet("Sachin")

# In programing we have two types of functions:
# 1- Perform a task
# 2 - Return a value

# round() is an example of second type. becasue it calculates it.


# def get_greet(first_name):
#     return (f"Hi {first_name}")


# message = get_greet("sach")
# print(message)

# calling like above decouples the output from the actual get_greet function.
# output can be used anywhere...


# def increment(number, by):
#     return number + by


# print(increment(2, by=1))

# OR
# result = increment(2, 1)
# print(result)

# Default parameters and options parameters

# Iterate over touple.


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total = total * number
#     return total


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user)


# save_user(id=1, name="Sach", age=42)

# where we use double astrics, we can pass multiple arguments.Which is dictionary.

# Local Variable - use these as much as possible.
# Scope - Scope of a variable, paramater etc inside the function only. i.e Local variables.

# Global Variable


# def multiplys(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiplys(2, 3, 4, 5))


# Break point add - Fn + F9
# F10 to run the program up to break point
# F11 to step into the function
# stop debugger Stop F5

# Command + / --> comments few lines...
# select a line and move up down.. Alt+arrow..

# Exercise

jkj
jkj
/
# Fizz_buzz algotrithm.

# def fizzbuzz(input):
#     if input % 3 == 0:
#         result = "Fizz"
#         print(result)
#     else:
#         result = "Buzz"
#         print(result)
#     return result


# fizzbuzz(9)

# Another way of doing the same.
# def fizzbuzz(input):
#     if input % 3 == 0:
#         result = "Fizz"
#     else:
#         result = "Buzz"
#     return result


# print(fizzbuzz(9))

# third way

# def fizzbuzz(input):
#     if input % 3 == 0:
#         return "Fizz"

#     return "Buzz"


# print(fizzbuzz(9))

# Another way


def fizzbuzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"


print(fizzbuzz(9))
