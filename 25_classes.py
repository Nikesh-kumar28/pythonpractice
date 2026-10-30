# what is class?
# a class is a blueprint or a templete for creating objects
# think of a class as a set of instructions for building sokething, likethe blueprint for a house
# the blueprint defines what the house will have-rooms, doors, windows-but it isnot the house itself
# we can use classes to create our custom datatypes

# In Python, a class defines the attributes (data) and methods (behaviors) that all objects of that class will share.
#     Attributes: These are the data or properties of an object. For a Car class, attributes could be color, brand, and mileage.
#     Methods: These are functions that an object can perform. For a Car class, methods could be start_engine(), drive(), or honk_horn().

# Defining a Class
# You define a class using the class keyword, followed by the class name (which, by convention, should start with a capital letter).

# class my_class:
#     ...

# creating object (instances) from a class

# object_name = my_class()

# print(type(object_name))

# a = int("45")
# print(type(a))

# int()
# float()
# tuple()
# set()
# dict()
# frozenset()
# str()
# bool()

# a = {1, 2, 3, 4, 5, 6}
# print(type(a))

# a = 1, 2, 3, 43, 4
# b = [4, 3, 2, 3, 5,3]

# print(45)

# print(a,b)

# class demo:
    
#     p = 56
#     q = 66
#     r = 78

# a = demo()

# print(a.p, a.q, a.r)

# class SocialMedia:

#     CEO = "Mark"

#     def like(self):
#        print("liked")

#     def comment(self):
#        print("liked")

# facebook = SocialMedia()

# print(facebook.CEO)
# facebook.like()

# class SocialMedia:

#     CEO = "Mark"

#     def like(self):
#         print("liked")

#     def comment(self):
#         print("liked")

# a = SocialMedia()
# b = SocialMedia()
# c = SocialMedia()
# d = SocialMedia()
# e = [a, b, c, d]

# facebook = SocialMedia()

# print(facebook.CEO)
# facebook.like()

# a = [23, 34, 45, 65, 657]
# a.reverse()
# print(a)

# class SocialMedia:

#     CEO = "Mark"

#     def  like(self):
#         print("liked")

#     def comment(self):
#         print("commented")

#     def post(self):
#         print("Posted")

# facebook = SocialMedia()
# twitter = SocialMedia()
# LinkedIn = SocialMedia()

# print(facebook.CEO)
# print(twitter.CEO)
# print(LinkedIn.CEO)

# twitter.CEO = "Elon Mask"
# LinkedIn.CEO = "Ryan"

# print(facebook.CEO)
# print(twitter.CEO)
# print(LinkedIn.CEO)

# class car:

#     color = "Black"
#     brand = "Rolls Royce"
#     milage = "3mph"

#     def engin(self):
#         print("RR Engin")

#     def drive(self):
#         print("driving")

#     def honk(self):
#         print("peeeeeeeeeeee")

# a = car()
# b = car()

# print(a.brand)
# print(b.brand)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.milage)
# print(b.milage)

# class dog:

#     species = "GS"

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# a = dog()
# a.eat()
# a.bark()

# class dog:

#     species = "GS"

#     def eat(self):
#         self.p = 50
#         print(f"hungry right now")

#     def bark(self):
#         print(self.p)
#         print(f"says wooof!")

# a = dog()
# a.eat()
# a.bark()

# class dog:

#     species = "Husky"

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# a = dog()
# c = dog()
# c.eat()
# c.bark()

# class user:

#     name = "nikesh kumar"
#     mob = "7426906170"
#     addr = "haryana"

#     def display_info(self):
#         print(self.name, self.mob, self.addr)

# data = user()
# print(data.name, data.mob, data.addr)
# data.display_info()

# Understanding Self


# Understanding the Self

# class Dog:

#     species = "GS"

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# a = Dog()

# c = Dog()
# c.eat()
# c.bark()


# class Dog:

#     species = "GS"

#     def test(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.c)
#         print(f"says woof!")

# xyz = Dog()
# xyz.test()
# xyz.eat()
# xyz.bark()



# class Hello:

#     def test(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40

#     def set_a_b(self):
#         self.a = 50
#         self.b = 100

#     def set_c_d(self):
#         self.c = 10
#         self.d = 20

#     def display_all(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#         print(self.d)

# xyz = Hello()
# xyz.test()
# abc = Hello()
# abc.test()
# xyz.set_a_b()
# abc.set_c_d()
# xyz.display_all()
# print("*"*80)
# abc.display_all()

# class dog:

#     species = "GS"

#     def eat(self):
#         self.age = 5
#         print(f"hungry right now")

#     def bark(self):
#         print(self.age)
#         print(f"says woof!")

# a = dog()
# a.eat()
# a.bark()

# Attributes (The "What It Is")
# Attributes are the data or properties associated with an object.
# They store information about a specific instance. 
# Think of them as variables that belong to an object.

# Methods (The "What It Can Do")
# Methods are the functions that belong to a class.
# They define the behaviors or actions an object can perform.
# They are essentially functions that are defined within a class.


# Constructor
# The __init__() Method (The Constructor)
# The __init__() method is a special method in a class. It's automatically called whenever a new object is created.
# Its primary purpose is to initialize the object's attributes with the values you provide. It's often called the constructor.
#     self: This is the first parameter of any method in a class. It's a reference to the specific object that is being created.
#  It allows you to access and modify the object's attributes and methods.


# class int:

#     species = "bwd"

#     def __init__(self):
#         self.age = 30
#         print("bhaiya object ban gya")

#     def eat(self):
#         self.age = 5
#         print(f"hungry right now")

#     def bark(self):
#         print(self.age)
#         print(f"says woof!")

# a = int()
# a.eat()
# a.bark()

# Constructor with Argument

class 