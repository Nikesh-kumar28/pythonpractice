# What is a Function?

# At its core, a function is a reusable block of code that performs a specific task. 
# Think of it as a small, self-contained machine. 
# You give it some input, it does its job, and then it can give you an output.

# Using functions makes your code:
#     Organized: Breaks down a large program into smaller, manageable pieces.
#     Reusable: You can call the same function multiple times without rewriting the code.
#     Easier to read and debug: If something goes wrong, you know exactly which "machine" to check.

# Type Of Functions:
    # Inbuilt Functions
    # Custom Functions

# Inbuilt Functions

# Every function has two main parts: the definition and the call.

# Defining a Function
# You define a function using the def keyword, 
# followed by the function name, parentheses (), and a colon :
# The code inside the function must be indented.

# syntax
# def function_name():
#     print("hello from inside this function!")
# function_name()

# def function_name():
#     print("jnbhebfcnsdnjc sd")
# function_name()

# def test():
#     print("i am line 1")
#     print("i am line 2")
#     print("i am line 3")
#     print("i am line 4")
#     print("i am line 5")
# test()

# def test():
#     print("i am line 1 of and func")
#     print("i am line 1 of and func")
#     print("i am line 1 of and func")
#     print("i am line 1 of and func")
#     print("i am line 1 of and func")
# test()

# a = 23
# b = 24
# print(a + b)

# def test_func():
#     print("hii i am the function.")
# test_func()
#     print("hi I am the function.")
#     print("hi I am the function.")

# def: A keyword that tells Python you're defining a new function.
# test_functiontion: A name you choose for your function. It should be descriptive and follow Python's naming conventions (lowercase with underscores).
# (): These hold the function's parameters (inputs). In this basic example, there are no parameters.

# Calling a Function
# To make the function run, you simply "call" it by writing its name followed by parentheses.

# example

# def greet():
#     print("welcome to python functions!")

# greet()

# a = int(input("enter a number. "))
# b = int(input("enter a number. "))
# print(a * b)

# def mul():
#    a = int(input("enter a number. "))
#    b = int(input("enter a number. "))
#    print(a * b)
# mul()

# write a function that take a number from keyboard and tell if it's odd or even

# def odd_even_check():
#     a = int(input("Enter A number: "))
#     if a % 2 == 0 :
#         print("Even")
#     else:
#         print("Odd")

# odd_even_check()

# Make a program with a function that check a number is divided by 3

# def div_checker_by_3():
#     a = int(input("Enter A Number: "))

#     if a % 3 == 0:
#         print("Yes it's divisible by 3")
#     else:
#         print("No it's not divisible by 3")

# div_checker_by_3()
# div_checker_by_3()

# Parameters and Arguments (Inputs)

# Functions often need to work with different pieces of data. 
# You can pass information into a function using parameters and arguments.
#     Parameters: The names you define in the function's parentheses when you create it. 
#     Arguments: The actual values you pass into the function when you call it.

# Example:

# def greet():
#     print(f"Hello, how are you?")
# greet()

# def greet( a ):
#     print(a)
#     print(f"Hello, how are you?")

# a=78
# greet(a)

# def add(a , b):
#     print(a + b)
# add("nikku", "yadav")
# add(5 , 60)

# def sub(a , b):
#     print(a - b)
# # sub(23 , 90)

# def mul(a , b):
#     print(a * b)
# mul(345 , 987654)

# a = int(input("enter x number "))
# b = int(input("wnter y number "))

# add(a , b)
# sub(a , b)
# mul(a , b)

# def odd_even_checker( number ):
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# odd_even_checker( int(input("enter a number: ")))

# write a function that takes a list of integers and prints the sum of all the elements

# def add_list()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

