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

# def add_list( data ):

#     sum = 0
#     for x in data:
#         sum = sum + x
#     print(sum)
# add_list( [1, 2, 3, 4, 5 ] )
# add_list( [1, 2, 3, 4, 5, 9, 10])
# add_list([ 5, 6, 7, 8, 9, 10 ])
# add_list( [3, 4, 5, 6, 7, 8, 9, 10 ])

# write a function that takes a list of integers and prints the largest number in list.

# def find_largest():
#     data = [ 234, 567, 23456, 5678, 234567, 12345678 ]
#     largest = data[0]

#     for x in data:
#         if x > largest:
#           largest = x
#     print(  largest)

# find_largest([ 234, 567, 23456, 5678, 234567, 12345678 ])

# doc string

# def cap_str( name ):

#     "this is a test function"

#     print(name.upper())

# cap_str("nikku")

# Functions with Multiple Parameters

# You can define a function with multiple parameters, 
# separated by commas. 
# The arguments you pass when calling it will be assigned to the parameters
# in the same order.

# Example:

# def calculate_sum(num1, num2):
#     total = num1 + num2
#     print(f"The sum is: {total}")

# calculate_sum(20, 30)
# calculate_sum( "Hello", " World!" )

# def test(a,b,c):
#     print( f"a: {a}, b:{b}, c:{c}" )

# test( 30, 20 ,10 )

# Positional and Keyword Arguments
# You can call a function in different ways based on how you pass arguments.

# Positional Arguments
# The arguments are matched to parameters based on their position or order. This is the method we've used so far.
# Example:

# def display_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# Order matters here!
# display_info("Charlie", 25) # "Charlie" is assigned to 'name', 25 to 'age'
# display_info(25, "Charlie")

# Keyword Arguments
# You can specify the argument's name when you pass it, which means the order doesn't matter.

# keyword argument
# You can specify the argument's name when you pass it, which means the order doesn't matter.

# def display_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# order doe not matter here!

# display_info(age = 25, name = "charlie")

# example

# def display_info(name, age, city, collage, number):
#     print(f"Name: {name}, Age: {age}, {city}, {collage}, {number}")

# display_info("Diana", 30, "jaipur", "ABC", "8709876")
# display_info(number = "98765", city = "jaipur", age = 30, name = "diana", collage = "xyz")

# mix of positional and keywords arguments
# display_info("nikku", 45, collage = "test", number = 2345, city = "sdfsdaf")
# display_info( name="Vipin", age=34, city="Jaipur", "XYZ", "9855884345" )
# display_info( name="vipin", 34, "Jaipur", "tets", 42424 )

