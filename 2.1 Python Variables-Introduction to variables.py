# is simply a container of value


# NAMING RULES

# 1. Can only begin with letter and underscore

# 9tyr = "ben 10"
# syntax error

flag = 7789
_9lives = "cat"

print(flag)
print(_9lives)

# 2. the rest of the identifier can contain letters, numbers and underscores
# _$$aapkipchumba = "billionaire"
# syntax error
_9076Kyu = "money"
print(_9076Kyu)

# 3. Case sensitive
name = "Symon"
# print(Name)
# Name is not defined

# 4. Reserved words (Keywords)  cannot be used as identifiers

# class =" Noise makers"
# print(class)
# invalid syntax


# keywords are colored orange in pycharm

# 5. Assinging and reassigning variables

# python is dynamically typed , no need to declare its type
symon = "789"
print(symon)
symon = 789
print(symon)
symon = 789.789
print(symon)
# you cannot use python variables before assigning its values


# cannot put identifier on the right side

# 789 = "symon"
# 789 = symon
# syntax error-cannot assign to literal


# 6 Multiple assignment

age, city, name, location = 28, "Nairobi", "Symon", "Baringo"

print(age);
print(city);
print(location)

print(f"{age}{city}{name}{location}")

# 7 Swapping variables

a, b = "red", "blue"
# intercahning values
a, b = b, a

print(a)
print(b)

# 8 Deleting variables
c = "colored"
del c
# print(c)
# c is not defined


