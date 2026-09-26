# a = {12, 34, 56, 788, 999, 45}
# print(a)

# b = {23, 45, 34, 34, 23, "345", 345}
# print(b)

# c = {23, 45, (34, 56, 78), 3, 2345, 23456, "23", "23"}
# print(c)

# a = {23, True, 1, False, 0}
# print(a)

# c = {23, 456, True, 1}
# print(c)

# c = {23, 456, 1, True}
# print(c)

# empty_set = set()
# print(empty_set, type(empty_set))

# a = { (), False }
# print(a)
# print(a[0])

# b = [ (), True]
# print(b)
# print(b[0])

# a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, "Nikku", "nikku", True, 0, 1, False}
# print(a)

# a = "rajasthan"
# my_set = set(a)
# print(my_set)

# a = (1, 1, 2, 2, 5, 6, 7)
# my_set = set(a)
# print(my_set)

# a = (2, 2, 2, 3, 4, 4, 5, 6, 7, 7, True, 1, 0, False)
# my_set = set(a)
# print(my_set)

# a = {12, 34, 123, (123, 34), "2345", 34.56, False, 0, 1, True}
# print(a)

# a = {12, 12, 12, 34, 56, 67, (12, 34), "8734", False, True, 87.09}
# print(a)

# a = {True, 1, 0, False, "7465", 98.90}
# print(a)

# a = 'haryana'
# my_set =  set(a)
# print(my_set)

# a = (1, 2, 1, 2, 3, 4, 5, 6, 7, 2, 34, 0, False)
# my_set = set(a)
# print(my_set)

# fruits = {"apple", "banana", "cheery", "banana", 1, 2, 3, 5, 6, 0, True, False}
# print(fruits)

# mixed set

# mixed_set = {"cheery", 1, "hello", (1, 2), 9.23, (1, 2)}
# print(mixed_set)

# my_set = {1, 2, 3}
# my_set.add((1, 2))
# print(my_set)

# my_set = {1, 2, 3, 4}
# my_set.add(("apple", "cheery"))
# print(my_set)

# my_set = {34, 56, 78, 89, 90}
# my_set.add((23, 456, 678))
# print(my_set)

# my_set = {34, 56, 678, 12345, 34567}
# my_set.update((1, 2, 3, 4, 5, 6, 7, 8))
# print(my_set)

# my_set = {123456, 12345, 123456, 123456, 123456}
# my_set.update(("uwf", "juhf", "uwed"))
# print(my_set)

# my_set = {1, 2, 3}
# my_set.add(("abcdef"))
# print(my_set)

# my_set = {1, 2, 3}
# my_set.update(("abcdef"))
# print(my_set)

# my_set = {1, 2, 3, 4, 5}
# my_set.remove((3))
# print(my_set)

# my_set = {1, 2, 3}
# my_set.remove((2))
# print(my_set)

# my_set = {10, 20, 30, 40, 50, 80}
# my_set.discard((50))
# print(my_set)

# my_set = {1, 2, 3}
# my_set.remove((9))
# print(my_set)

# my_set = {1, 2, 3}
# my_set.discard(("9"))
# print(my_set)

# my_set = {23, 50, 90, 80}
# my_set.discard((70))
# print(my_set)

# my_set = {1, 2, 3, "abc", (23)}

# data = my_set.pop()
# print(my_set)
# print(data)

# my_set = {23, 45, 67, 889}
# data = my_set.pop()
# print(my_set)
# print(data)

# a = {1, 2, 4}
# b = a
# a.add(67)
# print(a)
# print(b)

# a = {3, 4, 6}
# b = a.copy()
# b.add(79)
# print(a)
# print(b)

# my_set = {10, 20, 30, 40, 50}
# my_set.clear()
# print(my_set)

# my_set = {345, 456, 567, 789}
# my_set.clear()
# print(my_set)

# union 

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a.union(set_b))
# print(set_b.union(set_a))
# print(set_a | set_b) Pipe Operator

# intersection 

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a.intersection(set_b))
# print(set_b.intersection(set_a))
# intersection_set = set_a & set_b
# print(intersection_set)

# difference

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
#  print(set_a.difference(set_b))
# print(set_b.difference(set_a))
# print(set_a - set_b)
# print(set_b - set_a)

# symmetric_diffrence

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a, b, a.symmetric_difference(b))
# print(a, b, b.symmetric_difference(a))

# sub means choota
# sup means bada

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6}
# set4 = {8, 9}
# print(set1.issubset(set2))
# print(set3.issubset(set2))
# print(set1.issuper(set2))
# print(set2.issuperset(set1))
# print(set1 > set2)
# print(set2 > set1)


# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6}
# set4 = {8, 9}
# # print(set3.isdisjoint(set1))

# frozen set
# fs = frozenset((1, 2, 3, 1, 1, 2, 3))
# ns = set([1, 2, 3, 1, 1, 2, 3])
# print( dir(ns))

# | Feature                  | List                | Tuple             | Set             | Frozenset     | String         |
# | ------------------------ | ------------------- | ----------------- | --------------- | ------------- | -------------- |
# | **Syntax**               | `[ ]`               | `( )`             | `{ }`           | `frozenset()` | `' '` or `" "` |
# | **Ordered**              | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Mutable** (can change) | ✅ Yes              | ❌ No             | ✅ Yes          | ❌ No         | ❌ No          |
# | **Duplicates allowed**   | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Indexing possible**    | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Elements type**        | Any                 | Any               | Only hashable   | Only hashable | Characters     |
# | **Use case**             | Dynamic collections | Fixed collections | Unique elements | Immutable set | Text data      |




# sets question practice without loops

# How do you find the total number of unique elements inside a set?

# my_set = {10, 20, 30, 40, 50}

# print(len(my_set))

# Given two sets, how do you find elements common to both?
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.intersection(set2))

# How do you add a single element and multiple elements at once?
# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)

# numbers = {1, 2, 3}
# numbers.update([4, 5, 6])
# print(numbers)

# Given two sets, how do you get all unique elements from both combined?
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))

# How do you remove an element without raising an error if it doesn't exist?
# numbers = {1, 2, 3, 4}
# numbers.discard(5)
# print(numbers)

# How do you check if one set is a completely contained subset of another?
# set1 = {1, 2}
# set2 = {1, 2, 3, 4}

# print(set1.issubset(set2))

# How do you remove all elements to make a set empty?
# numbers = {1, 2, 3, 4, 5}
# numbers.clear()
# print(numbers)


# sets question with loops

# Write a program to iterate through a set and print each element multiplied by 10.
# numbers = {1, 2, 3, 4, 5}

# for num in numbers:
#     print(num * 10)

# Write a program to find the sum of all numbers in a set using a for loop.
# numbers = {10, 20, 30, 40, 50}
# total = 0
# for num in numbers:
#     total = total + num

# print("Sum =", total)

# Given a set of strings, use a loop to count how many elements have length greater than 4.
# words = {"apple", "cat", "banana", "dog", "python"}
# count = 0
# for word in words:
#     if len(word) > 4:
#         count = count + 1
# print("Count =", count)

# Write a program to filter out all odd numbers into a new set using a loop.
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# odd_numbers = set()
# for num in numbers:
#     if num % 2 != 0:
#         odd_numbers.add(num)
# print("Odd numbers:", odd_numbers)

# Given a list of sets, combine (union) all of them into a single set using a loop.
# sets = [
#     {1, 2, 3},
#     {3, 4, 5},
#     {5, 6, 7}
# ]
# result = set()
# for s in sets:
#     result = result.union(s)
# print(result)
