# What is a Dictionary?

# A dictionary is an unordered collection of items. Each item is stored as a key-value pair.
#     Unordered : Historically, dictionaries were unordered. From Python 3.7 onwards, dictionaries maintain insertion order.
#     Mutable: You can add, remove, and modify key-value pairs after the dictionary has been created.
#     Values can be anything: Values can be of any data type and can be duplicates.
#     Keys: Keys are the unique data in a dict and any immutable datatype can be a key
#     Mapping: Dictionaries are often referred to as "mappings" because they map keys to values.
#     We use the : operator to separate the key and value


# { <key>:<value> }

# a = [ "Berlin", 20, "9876545438", "Berlin"]
# b = [ "Rohit", 20, "98765438", "Jaipur"]

# a = { "name": "Rohit", "age": 20, "mob": "9876548765", "city": "Jaipur"}
# print(a)

# an empty dictonary
# empty_dict = {}
# print( type(empty_dict))

# person = { "name": "nikku", "age": 22, "city": "rewari"}

# person = {
#     "name": "nikku",
#     "age": 22,
#     "city": "rewari"
# }
# print(person)

# data = {
#     1: "nikesh",
#     2: 30,
#     3: "rewari",
#     3: "test"
# }
# print(data)

# mixed dict

# mixed_keys_dict = {
#     "name": "bob",
#     1: "one",
#     3.14: "pi",
#     (1, 2): "tuple key"
# }
# print(mixed_keys_dict)

# accesing value
# a = { "name": "nikku", "age": 21, "city": "rewari", "roll_number": 234567}
# print(a ["name"])
# print(a ["age"])
# print(a ["roll_number"])

# a = [ 1, [2, 3] ]
# print(a[1] [0])

# a = {
#     "name": "kvnfgjr",
#     "age": 34,
#     "city": "nbgdc",
#     "data1": {
#         "level": "advanced",
#         "data2": [1, 2, 3, 4, 5, {"data3": "dummy_data"}]
#     }
# }
# print(a["age"])
# print(a["data1"] ["level1"])
# print(a["data1"] ["data2"])
# print(a["data1"] ["level"].upper())
# print(a["data1"] ["data2"] [-1])
# print(a["data1"] ["data2"] [-1] [ "data3"])
# print(a["data1"] ["data2"] [-1] ["data3"] [-1])

# atm_network = {
#     "network_name": "GlobalCash ATM Network",
#     "status": "OPERATIONAL",
#     "terminal_id": "ATM_NY_4021",
#     "location": {
#         "branch": "Downtown Central",
#         "address": {
#             "street": "100 Financial Way",
#             "city": "New York",
#             "coordinates": {"lat": 40.7128, "lng": -74.0060}
#         }
#     },
#     "hardware_status": {
#         "card_reader": "FUNCTIONAL",
#         "receipt_printer": {
#             "paper_level": "LOW",
#             "ink_level": "OK"
#         },
#         "cash_cassettes": [
#             {"denomination": 10, "count": 150, "currency": "USD"},
#             {"denomination": 20, "count": 420, "currency": "USD"},
#             {"denomination": 50, "count": 80,  "currency": "USD"},
#             {"denomination": 100, "count": 210, "currency": "USD"}
#         ]
#     },
#     "current_session": {
#         "session_id": "SESS_982341",
#         "card_inserted": True,
#         "account_holder": {
#             "name": "Alex Mercer",
#             "customer_id": "CUST_99120",
#             "accounts": [
#                 {
#                      "account_type": "CHECKING",
#                      "account_number": "****5678",
#                      "balance": 3450.75,
#                      "daily_withdrawal_limit": 500.00
#                  },
#             ]
#         },
        
#     }
# }
# print(atm_network)
# print(atm_network["current_session"] ["account_holder"] ["name"])
# print(atm_network["current_session"] ["account_holder"] ["accounts"])
# print(atm_network["current_session"] ["account_holder"] ["accounts"] ["account_type"])

# adding and updating the data
# a = {"name": "berlin", "age": 34, "city": "newyork", "roll_number": 345}
# a["name"] = "rohit"
# a["mob"] = "098765"
# print(a)

# modifying dict
# grades = {"math": 90, "science": 85}
# print(grades["history"])
# grades["history"] = 78
# grades["math"] = 40
# print(grades)

# delete a key-value pair using del
# grades = {"math": 90, "science": 85}
# del grades["science"]
# print(grades)

# pop an item 

# grades = {"math": 90, "science": 85}
# popped_value = grades.pop("math")
# print(grades)

# missing_value = grades.pop("english", "not found")
# missing_value = grades.pop("science", "not found")
# missing_value = grades.pop("abc", "false")
# print(missing_value)

# grades = {"math": 90, "science": 85}
# popped_item_pair = grades.popitem()
# print(grades.popitem())

# grades.clear()
# print(grades)

# a = [1, 2, 3, 4, 5, 6, 6]
# i = 0
# length = len(a)
# while i < length:
#     print(i, a.pop())
#     i += 1
# print(a)

# basic dict operation
# profile = {
#     "name": "vikash",
#     "age": 34,
#     "gender": "male"
# }
# print(len(profile))

# a = {
#     "name": "mohit",
#     "age": 45,
#     "city": "gurugram",
#     "data1": {
#         "level": "advance",
#         "data2": [1, 2, 3, 4, 5, { "data3":"dummy_value"}]
#     }
# }
# print(len(a))

# membership oper.

# profile = {
#     "name": "vikash",
#     "age": 25,
#     "gender": "male"
# }
# print(25 in profile)
# print("age" in profile)

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# # d1.update(d2)
# d2.update(d1)
# # print(d1)
# print(d2)

# data = {"name": "nikk", "age": 25}
# print(data["age"])
# print(data.get("mob."))
# print(data.get("mob.", "not found"))

# data = { "name": "nikku", "age": 23,}
# data["city"] = "jaipur"
# print(data)

# data = { "name": "nikku", "age": 23}
# email = data.setdefault("email", "nixxx@gmail.com")
# print(data)

# a = {"rohit", "vikash", "arvind", "vipin"}
# new_dict = dict.fromkeys("jaipur", "raj")
# print(new_dict)

# company = {
#     "ceo": {
#         "name": "john doe",
#         "department": "executive"
#     },
#     "employes": {
#         "101": {
#             "name": "pritam",
#             "role": "engineer"
#         },
#         "102": {
#             "name": "priya",
#             "role": "designer"
#         }
#     },
#     "depertments": ["hr", "engineer", "design"]
# }
# print(company.get("employes").get("101").get("name", 20))
# print(company.get("employes").get("101").get("age", 20))
# print(company.get("depertments") [-1])
# print(company.get("employes").get("1023", "hello").upper())
# print(company.get("employes").get("102", "hello").upper())

# person = { "name": "nikku", "age": 22, "city": "rewari"}
# print(person.keys())
# print(person.values())
# print(person.items())

# person = { "name": "nikku", "age": 22, "city": "rewari"}
# for x in person:
#     print(x)

# for x in person.keys():
#     print(x)

# for x in person.values():
#     print(x)

# for x in person.items():
#     print(x)
#     print(x[0])


# person = { "name": "nikku", "age": 22, "city": "rewari"}
# for x , y in person.keys():
#     print(x, y)

# a = {"name", "age", "city", "mob", "vipin", "jaipur", "india"}
# a = {23, 24, 6, 75, 75, 67, 34, 243, 56, 234, 76, 45, 457, 90}

# With Loops
# Iterate through a dictionary and print all its keys.
# a = {"name", "age", "city", "mob", "vipin", "jaipur", "india"}
# b = {23, 24, 6, 75, 75, 67, 34, 243, 56, 234, 76, 45, 457, 90}
# print({ x:y for x,y in zip(a,b)})

# data = {
#     'mob': 34,
#     'age': 67,
#     'india': 90,
#     'vipin': 6,
#     'jaipur': 457,
#     'city': 234,
#     'name': 75
# }
# for x in data.keys():
# for x in data:
    # print(x)

# a = list( data.keys() )
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# Iterate through a dictionary and print all its values.
# data = {
#     'mob': 34,
#     'age': 67,
#     'india': 90,
#     'vipin': 6,
#     'jaipur': 457,
#     'city': 234,
#     'name': 75
# }
# for x in data.values():
    # print(x)

# a = list( data.values() )
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# Print both keys and values side-by-side using a loop.
# data = {
#     'mob': 34,
#     'age': 67,
#     'india': 90,
#     'vipin': 6,
#     'jaipur': 457,
#     'city': 234,
#     'name': 75
# }
# for x in data:
#     print(x, data[x])
#     (data[x])

# Given items and prices, calculate total cost of all items using a loop.
# grocery_prices = {
#     "apple": 10,
#     "banana": 20,
#     "milk": 30,
#     "bread": 40,
#     "eggs": 50,
#     "rice": 60
# }
#  price = list(grocery_prices.values())
# print(price)

# sum = 0
# for x in price:
#     sum += x
#     print(sum)

# sum = 0
# for x in grocery_prices:
#     print(sum, grocery_prices[x])
#     sum = sum + grocery_prices[x]

# Create a dictionary where keys are 1–5 and values are squares using a while loop.
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }
# data = {}
# i = 1
# while i <= 5:
#     data[i] = i * i
#     i += 1 
# print(data)

# data = {}
# i = 1
# while i <= 5:
#     data.setdefault(i, i ** 2)
#     i += 1
# print(data)

# data = {}
# for x in range(1, 6):
#     data[x] = x * x
#     print(data)

# Filter out items where the value is an even number into a new dictionary.
# orignal_dict = {
#     "apple": 1,
#     "banana": 2,
#     "cheery": 3,
#     "date": 4,
#     "elderberry": 5
# }
# for x in orignal_dict:
#     if orignal_dict[x] % 2 == 0:
#         print(x)

# Find the key with the highest value using a loop.
# prices = {
#     "mouse": 25,
#     "laptop": 1200,
#     "monitor": 300,
#     "keyboard": 75,
#     "headset": 100
# }
# a = [25, 1200, 300, 75, 100]
# largest = a[0]
# for x in a:
#     if x > largest:
#         largest = x
# print( largest)        

# largest_value = 25
# largest_value_key = "mouse"

# for x, y in prices.items():
#     if y > largest_value:
#         largest_value = y
#         largest_value_key = x
# print(largest_value, largest_value_key)


# Swap keys and values using a loop.
# prices = {
#     "mouse": 25,
#     "laptop": 1200,
#     "monitor": 300,
#     "keyboard": 75,
#     "headset": 100
# }
# data = {}

# for x, y in prices.items():
#     data[y] = x
#     print(data)


# Merge two dictionaries manually using a loop.
# qna_batch_1 = {
#     "question1": "what is python?",
#     "question2": "what is an ide?"
# }

# qna_batch_2 = {
#     "question2": "an integrated development environment",
#     "question3": "what is a loop"
# }
# qna_batch_1.update(qna_batch_2)
# print(qna_batch_1)

# for x , y in qna_batch_2.items():
#     qna_batch_1[x] = y
#     print(qna_batch_1)


# Without Loops

# How do you access a value safely without causing a KeyError?
# student = {"name": "Nikesh", "age": 20}
# print(student.get("marks"))

# How do you find the total number of key-value pairs?
# student = {
#     "name": "Nikesh",
#     "age": 20,
#     "course": "Python"
# }
# print(len(student))

# How do you add or update a key-value pair?
# student = {"name": "Nikesh", "age": 20}
# student["city"] = "Jaipur"   
# student["age"] = 21          
# print(student)

# How do you remove a key and return its value at the same time?
# student = {
#     "name": "Nikesh",
#     "age": 20,
#     "city": "Jaipur"
# }
# age = student.pop("age")
# print(age)
# print(student)

# How do you check if a key exists without loops?
# student = {"name": "Nikesh", "age": 20}
# print("name" in student)

# How do you clear all items from a dictionary?
# student = {"name": "Nikesh", "age": 20}
# student.clear()
# print(student)

# Given two dictionaries, how do you merge them in a single line?
# dict1 = {"name": "Nikesh"}
# dict2 = {"age": 20}
# result = dict1 | dict2
# print(result)

# How do you extract all keys into a list without a loop?
# student = {
#     "name": "Nikesh",
#     "age": 20,
#     "city": "Jaipur"
# }
# keys = list(student.keys())
# print(keys)

# Given a list of keys, how do you create a dictionary with default value 0 in one step?
# keys = ["name", "age", "city"]
# student = dict.fromkeys(keys, 0)
# print(student)

# How do you create a shallow copy of a dictionary?
# student = {
#     "name": "Nikesh",
#     "age": 20
# }
# new_student = student.copy()
# print(new_student)

    