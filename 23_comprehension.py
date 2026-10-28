# print("hello world") ; print("hello") ; print("world") 

# one linear if else

# num = 3

# if num > 5:
#     print("yes")

# if num > 5: print("yes")

# if num > 5:
#     print(True)
# else:
#     print(False)

# print(True) if num > 5 else print(False)

# onelinear if else me colon nhi aata h
# one liner if k andar colon aata h 

# num = 4
# a = True if num > 5 else False
# print(a)

# for x in "hello": print(x)
# for x in range(1, 101, 2): print(x)

# for x in range(1, 11): print("div by 5") if x % 5 == 0 else print("not div by 5")

n = -23

# if n > 0:
#     print("+ve")
# elif n < 0:
#     print("-ve")
# else:
#     print(0)

# print("+ve") if n > 0 else print("-ve") if n < 0 else print(0)

# num = 80

# if num % 3 == 0 and num % 5 == 0:
#     print("both")
# elif num % 3 == 0:
#     print("3")
# else:
#     print(5)

# div_5 = num % 5 == 0
# div_3 = num % 3 == 0
# print("both") if div_5 and div_3 else print("3") if div_3 else print("5") if div_5 else print("none")

# List comprehension

# write a program to square each elements of the given list into a new list

# old_list = [2, 3, 4, 1, 6, 7]

# new_list = []
# for x in old_list:
#     new_list.append(x * x)
# print(new_list)

# print([ x * x for x in old_list  ])

# print([ x for x in range(0, 12, 2)])

# square = []
# for i in range(10):
#     square.append(i * i)
# print(square)

# squares = [i * i for i in range(10)]
# print(squares)

# data = [23, 43, 23, 11, 34, 56, 7, 8, 12, 15, 18, 33]
# new_list = []
# for x in data:
#     if x % 2 == 0:
#         new_list.append(x)
# print(new_list)

# print([ x for x in data if x % 2 == 1] )
# print([ x for x in data if x % 2 == 0] )

# data = [23, 45, 678, 89,90987, 567, 54, 45, 56]
# new_list = []
# for x in data:
#     if x % 2 == 0:
#         new_list.append(x)
# print(new_list)

# print([ x for x in data if x % 2 == 1])
# print([ x for x in data if x % 2 == 0])

# a = [ 23, 43, 23, 11, 34, 56, 7, 8, 12, 15, 18, 33]

# for x in a:
#     if x >= 18:
#         print(x)

# print([ x for x in a if x >= 18])

# even_numbers = { i for i in a if i % 2== 0}
# print(even_numbers)

# print([ x for x in a if x < 18])

# new_list = []
# for i in range(10):
#     if i % 2 == 0:
#         new_list.append(i * i)
# print(new_list)

# get the aquare of only the even numbers

# squares_of_even = ["Even" for i in range(10) if i % 2 == 0]
# print(squares_of_even)

# new_list = []
# for i in range(11):
#     if i % 2 == 0:
#         new_list.append("Even")
#     else:
#         new_list.append(i)
# print(new_list)

# print([ "Even" if x % 2 == 0  else "odd"for x in range(11) ] )
# print(new_list)

# students= [13, 40, 56, 90, 15, 80, 56, 43]
# print([i for i in students if i >= 33])
# print([i for i in students if i < 33])
# print(["pass" if i >= 33 else "fail" for i in students])

# dictonary comprehension 

# salaries = [25000, 60000, 45000, 80000, 350000, 950000]

