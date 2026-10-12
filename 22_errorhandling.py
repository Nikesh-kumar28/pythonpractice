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

 