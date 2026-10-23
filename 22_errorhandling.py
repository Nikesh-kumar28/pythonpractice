# errors are an unavoidable part of programming
# error handling is the process of anticipating and managing these errors
# so your program doesn't crash unexpectedly
# In Python, this is primarily done using exception handling.

# An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions.

# The try...except Block
# The try...except block is the fundamental tool for handling exceptions. It works like this:
#     The code inside the try block is executed normally.
#     If an exception occurs within the try block, 
#     the rest of the try block is skipped.
#     The program then looks for an except block that matches the type of exception that occurred.
#     The code inside the matching except block is executed.

# number = int(inpit("enter a number: "))

# try:
#     number = int(input("enter a number: "))
# except: 
#        print("please enter only integers.")

# try:
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 2: "))
#     print(a*b)
# except:
#     print("there is an error from our side we are working on fixing it.")

# try:
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 2: "))
#     print(a / b)
# except:
#     print("you can not divide any number by 0.")

# try:
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 2: "))
#     print(a + b)
# except:
#     print("you can not divide any number by 0.")

# try:
#     number = int(input("enter a number: "))
# except:
#     print("please enter only numbers")

# try:
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 2: "))
#     print(a*b)
# except:
#     print("there is an error from our side we are working on fixing it.")

# a_str = 36
# a_int = 35

# try:
#     if a_str > a_int:
#         print("yes they are equal.")
# except:
#     print("there is an error.")

# try:
#     a = int(input("enter a number: "))
#     b = int(input("enter a number: "))
#     print(a / b)
# except ValueError:
#     print("please enter only numbers")
# except ZeroDivisionError:
#     print("you can not divide any number by 0.")

# try:
#     a = int(input("enter a number: "))
#     b = int(input("enter a number: "))
#     print(a / b)
# except ValueError:
#     print("please enter only numbers")


# try:
#     a = int(input("enter a number: "))
#     b = int(input("enter a number: "))
#     print(a / b)
# except:
#     print("something is wrong.")
# finally:
#     print("i will run on both case.")

# Common Exception Types

# Python has many built-in exceptions to handle different types of errors. It's good practice to handle specific exceptions rather than a general one. Some of the most common exceptions are:
#     ZeroDivisionError: Raised when you divide by zero.
#     TypeError: Raised when an operation is performed on an object of an inappropriate type (e.g., adding a string and an integer).
#     ValueError: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert "hello" to an integer with int("hello")).
#     NameError: Raised when a variable is not found.
#     IndexError: Raised when a sequence index is out of range.
#     KeyError: Raised when a dictionary key is not found.
#     FileNotFoundError: Raised when a file cannot be found.

# try:
#     my_list = [0, 1]
#     user_input = int(input("enter an index: "))
#     print(my_list[user_input])
# except (IndexError ,ValueError) :
#     print("there is an  error")

# try:
#     my_list = [0, 1]
#     user_input = int(input("enter an index: "))
#     print(my_list[[user_input]])
# except (IndexError, ValueError) as x:
#     print(x)

# The else and finally Clauses
# The try block can have two optional clauses: else and finally.
#     The else block runs only if the code in the try block completes without any exceptions. This is a great way to separate the code that might fail from the code that depends on it succeeding.
#     The finally block runs no matter what. It's executed whether an exception occurred or not. This is perfect for cleanup operations like closing files or network connections.



# try:
#     a = int(input("Enter A number: "))
# except:
#     print("Type conversion error.")
# else:
#     print("No error")
# finally:
#     print("I will run at all cost.")

# """
# this is a test file.
# """

# for x in range(10):
#     print(x)
# else:
#     print("this is your output")

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("test")

# age = 16

# if age > 18:
#     print("yes you can vote")
# else:
#     raise ValueError("no you can not vote"
