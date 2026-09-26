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

