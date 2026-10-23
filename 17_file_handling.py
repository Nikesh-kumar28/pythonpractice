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

# +r
# +w
# +a
# +rb
# +wb
# +ab

# +r advantage is vo new file bna deta h agr koi file na ho tab
# +a advantage is vo new file nhi bnata agr koi file na ho 
# +a file nhi h new bna dega or file h content delete nhi kre ga read bhi kre ga write bhi kre ga

# with open("abcd.text", "+r") as a:
#     print(a.readable())
#     print(a.writable())

# open file in read mode. read content; count vowels like a string problem. close/ use with open

# vowels = 0
# with open("abcd.text") as a:
#     data = a.read()
#     for x in data:
#         if x in "aeiouAEIOU":
#             vowels += 1
# print(vowels)

# count the total number of words in a file.

# space = 0
# with open("abcd.text") as a:
#     data = a.read()
#     for x in data:
#         if x in " " or x == "\n":
#             space += 1
# print(space + 1)

# words = 0
# with open("abcd.text") as a:
#     data = a.readlines()
#     for x in data:
#         words += len(x.split())
#         print(words)

# Read a text file and count the total number of vowels in it?
# vowels = 0
# with open("abcd.text") as a:
#     data = a.read()
#     for x in data:
#         if x in "aeiouAEIOU":
#             vowels += 1
# print(vowels)

# Count the total number of words in a file?
# words = 0
# with open("abcd.text") as a:
#     data = a.readlines()
#     for x in data:
#         words += len(x.split())
#         print(words)

# Count the total number of lines present in a text file?
# with open("sample.text") as fobj:
    # print(fobj.read().count("\n"))
    # print(len(fobj.readlines()))

# Display only the lines in a file that contain the word "India"?
# with open("sample.text") as a:
#     all_lines = a.readlines()
#     for x in all_lines:
#         if  "India" in x:
#             print(x)

# Find the longest line in a text file?
# with open("sample.text") as a:
#     all_lines = a.readlines()
#     for x in all_lines:
#         print(len(x))

# with open("sample.text") as a:
#     all_lines = a.readlines()

#     largest_line = all_lines[0]
#     largest_line_len = len(all_lines[0])

#     for x in all_lines[1:]:
#         len(x) > largest_line_len
#         largest_line = x
#         largest_line_len = len(x)
# print(largest_line, largest_line_len) 

# Take a word from the user and count how many times that word appears across an entire file?
# with open("sample.text") as a:
#     content = a.read()
#     data = input("enter what you want to find: ")
#     print(content.count(data))

# Take 5 words from the user and count how many times each word appears across an entire file?
# with open("sample.text") as a:
#     content = a.read()
#     data = input("enter what you want to find: ")
#     data = input("enter what you want to find: ")
#     data = input("enter what you want to find: ")
#     data = input("enter what you want to find: ")
#     data = input("enter what you want to find: ")
   
#     print(content.count(data))
#     print(content.count(data))
#     print(content.count(data))
#     print(content.count(data))
#     print(content.count(data))

# Copy non-blank lines from a source file into a clean list of data?
# with open("sample.text") as a:
#     all_lines = a.readlines()
#     for x in all_lines:
#         if x != "\n":
#             print(x)

# Count the total number of blank lines in a text file?
# with open("sample.text") as a:
#     all_lines = a.readlines()
#     counter = 0
#     for x in all_lines:
#         if x == "\n":
#             counter += 1

# print(counter)

# Find and display the shortest non-blank line in a text file?

# with open("sample.text") as a:
#     all_lines = a.readline()

#     shortest_line = all_lines[0]
#     shortest_line_len = len(all_lines[0])

#     for x in all_lines[1:]:
#         len(x) < shortest_line_len
#         shortest_line = x
#         shortest_line_len = len(x)
# print(shortest_line, shortest_line_len) 

# how to copy a file    
# with open("sample.text") as a:
#     file_content = a.read()

# with open("new.txt", "w") as a:
#     a.write(file_content)

# with open("sample.text") as a:
#     file_content = a.readlines()

#     with open("new.txt", "w") as b:
#        i = 0
#        while i < len(file_content):
#         b.write(f"Line {i+1}: {file_content[i]}")
#         i += 1

