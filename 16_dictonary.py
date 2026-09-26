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

