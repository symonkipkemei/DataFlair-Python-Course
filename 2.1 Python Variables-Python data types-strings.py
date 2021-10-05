# String is a sequence of characters
# delimited by single or double quotes

name = "Kipchumba"
print(type(name))

# 1. SPANNING A STRING ACROSS LINES
# use triple quotes

love = """Love is a misconception between
the body, mind and the soul,
the gap through which information flows 
effortlessly"""
print(love)


# 2. DISPLAYING PARTS OF A STRING
# using index
life = "Happiness"
print(life[0])

# using slicing operator[]
print(life[4:10])

# 3. STRING FORMATTING
# you want to print both values and characters at once

# 3.a % operator
# 3.b format method
# 3.c f-strings


# 3.c f-strings

love = "perpertual Love"
happiness = "to allow part of yourself to connect with someone else"

print(f"I like {love} but I prefer {happiness}")


# CONCATENATE STRINGS
# joining strings together without gaps. The string becomes one

# not that you can concatenate strings but not strings with any other data type
a= "78"
b = "98"

print(a+b)