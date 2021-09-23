# SYNTAX STRUCTURE IN PYTHON

# 1. PYTHON LINE STRUCTURE
print("I am composed of logical lines")
print("a ne token follows each of those")

# 2.PYTHON MULTILINE STRUCTURE

# Double quotes on string in every new line
# makes it readable but does not create a paragraph


print("HI "
      "how are you symon")

print("\n")

# Backward slash allows code
# to be readable in many lines
# but does not create paragraphs


print("Hi \
how are you symon")

print("\n")

# putting strings in triple quotes allows
# you to create paragraphs

print("""How are you
kiplelgo
I miss you""")


# 3 PYTHON COMMENTS
# This is a comment
# We are declared by an octo-thorpe(#)
# Every single line has to start with
# octothorpe


# 4 PYTHON DOCSTRINGS

# A documentation string used to explain code
# mostly used at the beginning of a function

def greetings():
    """This code is used to print hi"""
    print("am happy to be here today")


# 5 PYTHON INDENTATION

# Used to delimit a block of code
if 2 > 6:
    print("success is taught")
else:
    print("Success is elf taught,\n"
          "you have to take it\n"
          "with your own hands\n")

# using triple quotes to print a statement is best only for un- indented line
print("""I did not know this is going to be a slow process
I hope it gets better""")

# 6 MULTIPLE STATEMENTS IN ONE LINE
# you can fit multiple statements within one line
# By separating statements with a semi-colon
# even though this grammar is acceptable, I will advice you to separate
# statements into their own individual lines
a = 45;
print(a)

# 7 PYTHON QUOTATIONS
# For string literals, If delimit with a single quotations, so be it to the end
# Be consistent
print("Symon we need to be more consistent\n"
      "It is fun this way")

print('Only the disciplined ones in life are free')

# 8 PYTHON BLANK LINES
print("we ignore blank lines")

# 9 PYTHON IDENTIFIERS
# I am a name of a program element and I am user defined
# We are classes, variables, functions, lists and dictionaries


# for classes, start with a capital letter.
# the rest, always start with a small letter.

# I am case sensitive and you cannot use certain words that have been reserved

# private identifiers starts with a leading underscore
# strongly private identifiers follow with double underscores
# special identifiers end with two leading underscores

# 10 PYTHON VARIABLES

# I become a store when I am assigned a value
# Because python is dynamically typed,
# I can hold any type of value dynamically at the point of assignment

cow = " a big animal that produces milk"
cow = 345
cow = ["fresian", "jersey", "ankole bulls", " Museveni bulls"]

print(cow)
# 11 STRING FORMATTERS

# We are used to concatenating strings ,
# but the problem is they have to be all to be strings
# for a long time we have been converting values into strings so
# that we can print them as one statement

# There is a solution for this
# FORMATTING


# these are the variables that we are going to format
x = 50000.09
value = "free"

# % operator method

print("I just need %s cash to be %s" % (x, value))

# format method
print("I just need {0} cash to be {1} ".format(x, value))

# the advantage of format method is you do not need to specify the type of data you are  printing


# f-string method
# this is the shortest way of formatting
# this what the industry is using
print("\n")
print(f"I just need {x} cash to be {value}")

# it is the shortest because  we directly input the values into the curly brackets
# instead of using representatives


# TAKE-AWAY

# Triple quotes multiline statements
# string formatters
# identifiers
# Multiple statements in one line
# Multiline comments amd docstrings

# LEFT-OVERS
# This is code is unreachable
