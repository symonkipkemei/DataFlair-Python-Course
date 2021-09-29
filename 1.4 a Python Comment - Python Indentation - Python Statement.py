# 1. Multiline Python Statement
# spanning a statement over several lines
# we use backslash to span a statement into several lines

# Eg. 01
print( \
    "Today is a good day")

# Eg. 02

a = 2 + \
    3 \
    + \
    5
print(a)

# 2. Multiple Python Statement in One Line
# we use a semi-colon to document more than one statement in one line


# Eg. 01
a = "I am going to town today";
b = "kipchumba is asleep"

# Eg. 01
print(a);
print(b)

# 3. Strings Python Statements

# declared either using double or single quotes

a = "Awinja is funny"
b = 'Kipchumba is funnier'

# this syntax is wrong, use double quotes outside followed
# by single quotes inside

print(' I hate mangoes "sana" ')

# 4. Blank Lines Python Statements

e = 10

f = 5

c = e + f

# note their is no space between f and the double quotes for the f formatter
print(f"I skip blank statements but i always print my answers {c}")

# Python Indentation
z = 6
if z > 10:
    print("hello")

# Python Comment

# I am a comment
print("The line above is a comment")

# 1. Multiline Python Comment


# using hash

# we can
# use hash several times
# or once


# using quotes
"This " \
"comment is spanned across" \
"many lines"

""" This
comment is spanned across
many lines"""



# DocString
# declared by triple quotes

def sayHi():
    """This function print hello message to your dear"""
    print("Hello love\n"
          "Nakupenda pia ")

sayHi()

sayHi.__doc__



