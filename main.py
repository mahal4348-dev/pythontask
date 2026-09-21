# Python is an indent based programming language
teams = ['Data', 'AI', 'DevOps']
for t in teams:
     print('Hello', t, 'Team from Inceptez Technologies')
     print('Keep Learning and Exploring!')

# Commented line in Python
# Inceptez Technologies Training Tracker

students = 100
trainers = 2

# Calculate the total number of students and trainers
total = students + trainers

print(total)


"""
This is a multi-line comment.
It describes the training tracker program.
It stores students and trainers and calculates the total.
"""


# Dead code - currently inactive
# print("Welcome to Inceptez Python Learning")

# Use Case 1: Playing with Quotes

str1 = 'This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'

str2 = "This is Inceptez's \"Python\" class for Data Engineers & AI Engineers"

str3 = """This is Inceptez's "Python" class for Data Engineers & AI Engineers"""

str4 = '''This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'''
print(str1)
print(str2)
print(str3)
print(str4)

# Use Case 2: Multiline String

message = """Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey."""

print(message)

#case sensitivity
name = 'maha'
Name = 'anu'
print(name)
print(Name)
#index
print(name[0])
print(name[0:2])

# index single
name = ("maha")
print(name[0])
print(name[0:3])

# index multi string
name = ("anu","maha","lubu")
print(name[0])
print(name[0:2])

#index single number
#age=21 Single value(int) → indexing panna mudiyathu
#print(age[0])
#Single-value tuple
age=(21,)
print(age[0])

#Multiple-value tuple
age=(21,22)
print(age[1])


#Sequence single string
name = ("anu")
for i in name:
    print(i)

# Sequence multi string
name = ("maha","lubu","anu")
for i in name:
    print(i)

#sequence single int
age = ("21")
for i in age:
    print(i)

age = (21,23)
for i in age:
    print(i)

#test