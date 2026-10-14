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

# Write a function that takes a list and an element as
# input and prints "Found" if the element exists in the list, otherwise prints "Not Found".

# a = [1, 2, 3, 5, 3, 2, 23, 23, 23, 54, 65, 86]

# what_to_find = 23

# for x in a:
#     if x == what_to_find:
#         print("found")
#     else:
#         print("not found")

# def value_checker(a, b):
#     temp = False

#     for x in a:
#         if x == b:
#             temp = True
#             break
#     if temp:
#        print("found")
#     else:
#        print("not found")

# value_checker( [1, 2, 3, 5, 3, 2, 23, 23, 23, 54, 65, 86],  233)

# Write a function that takes
# a list of integers and prints how many even numbers are present in the list.

# def value_checker(a):

#     temp = 0
#     for x in a:
#         if x % 2 == 0:
#             temp += 1
#     print(temp)
# value_checker( [1, 2, 3, 5, 3, 2, 23, 23, 23, 54, 65, 86])

# Write a function that takes a list of integers and returns the count of even numbers present
# in the list.

# def value_checker(a):

#     temp = 0
#     for x in a:
#         if x % 2 != 0:
#             temp += 1
#     print(temp)
# value_checker( [1, 2, 3, 5, 3, 2, 23, 23, 23, 54, 65, 86])

# Write a function that takes a list of integers and prints the average of all the numbers.

# def value_checker(a):
#     sum = 0
#     for x in a:
#          sum = sum + x

#     print(sum/len(a))
# value_checker([60, 90, 30, 50, 80])

# write a function that takes a list of integers and prints the count of positive numbers and
# negative numbers separately.

# def value_checker(a):
#     pos = 0
#     neg = 0
#     for x in a:
#         if x > 0:
#             pos += 1
#         else:
#             neg += 1
#     print(pos, neg)
# value_checker([60, 90, 30, 50, 80, -23, -34, -23, -35, -23, -35])

# def count_numbers(numbers):
#     positive = 0
#     negative = 0

#     for num in numbers:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1

#     print("Positive numbers:", positive)
#     print("Negative numbers:", negative)


# numbers = [10, -5, 20, -8, 0, 15, -3]
# count_numbers(numbers)

# Write a function that takes a list of integers and prints the factorial of each element.

# data = [5, 10, 15, 5, 23]

# def fact(n):
#     mul = 1
#     for x in range(1, n + 1):
#         mul = mul * x
#     print(mul)

# for x in data:
#     fact(x)

# def greet(name):
#     print(f"Hello {name}, How Are You?")

# greet("nikku")


# Example:
# def greet_with_default( name, message="Hello"):
#     print(f"{name}, {message}!")

# greet_with_default("Eve", "Good Afternoon")
# greet_with_default("Eve")
# greet_with_default("Frank", "Good morning")
# greet_with_default(message="Good Evening", name="Mumbai")

# def display_info(name, age, course, city="Jaipur", collage="ABC", collage_nu=66543):
#     print(f"Name: {name}, Age: {age}, City: {city}, Collage: {collage}, {collage_nu}, Course: {course}")

# display_info("vipin", age=23, course="BCA")

# Variable-Length Arguments (*args and **kwargs)
# Sometimes you don't know how many arguments a function will receive. Python handles this with special syntax.
# *args (Non-Keyword Arguments)
# The *args syntax allows a function to accept a variable number of non-keyword arguments. These arguments are bundled into a tuple inside the function.

# example

# def calculate_average(*numbers):
#     print(f"the average is: {numbers}")

# calculate_average()
# calculate_average(10, 20)
# calculate_average(10, 20, 30)
# calculate_average(10, 20, 30, 4550, 345, 'wefgh', 'sdfg', 234, 'wert')

# def mix_func(*a, b, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# mix_func(23, 10, 20, 30, 45, 567, 567)
# mix_func(23, 45, 56, 5456, 234, 567, c = 23, b = 10, d = 56)

# def test(p, q, *r):
#     print(p)
#     print(r)
#     print(q)

# test("jaipur", "alwar", "delhi", "mumbai", "pune")

