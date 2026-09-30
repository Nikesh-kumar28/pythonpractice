# File Handling Basics

# File handling in Python allows your programs to read data from and write data to files
# on your computer's storage.
# This is essential for storing information permanently, 
# so it isn't lost when your program finishes.

# the open function

# name = input("enter your name: ")
# age = input("enter your age: ")
# number = input("enter your number: ")
# print(name, age, number)

# a = open("Desktop/class/del.txt")
# print(a.read())

# a = open("rel.txt")
# print(a.read())

# a = open("jos.txt")
# file_data = a.read()
# print(file_data.count("print"))

# print(a.readable())
# print(a.writable())

# data = a.read()
# print(data.upper())

# a = open("jos.txt")
# b = a.readline()
# print(b)

# c = a.readline()
# print(c)

# d = a.readline()
# print(d)

# print(a.readline())
# print(a.readline())
# print(a.readline())
# print(a.readline())
# print(a.readline())

# a = open("test.txt")
# print(a.readline())
# print(a.readline())
# print(a.readline())
# print(a.readline())
# print(a.read())

# a = open("test.txt")
# a.read()
# a.seek(11)
# print(a.read())

# print(a.readlines())

# data = a.readlines()
# print(data[-1])

# a = open("6_ifelse.py")
# data = a.read()
# print(data.count("if"))
# print(data.count("elif"))

# a = open("13_lists.py")
# print(a.read())
# a.close()

# with open("test.txt") as a:
#     print(a.readable())
#     print(a.read())

# with open("test.txt") as a:
#     data = a.read()
#     print(data.count("India"))

# a = open("test.txt", "r")
# print(a.read())
# a.close()

# with open("test.txt", "r") as a:
#     print(a.read())

# a = open("abcd.text", "w")
# print(a.readable())
# print(a.writable())

# with open("abcd.text", "w") as a:
#     a.write( "hello" )

# with open("abcd.text", "w") as a:
#     a.write( "I am from delhi.\nhello delhi" )

# data = [ "line1\n", "line2\n", "line3\n", "line4", "ASDfae" ]
# a = open("abcd.text", "w")
# a.writelines(data)
# a.close()

# with open("abcd.text", "a") as a:
#     a.write( "I am from delhi.hello delhi.\n" )

# a = open("C:/Users/ny006/Videos/honey.mp4", "wb")
# a.close()

