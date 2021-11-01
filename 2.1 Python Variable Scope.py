print("Testing todays class")

# Today we are going to learn about the python scope
# in my own view, it is the extent to which the variable is applicable
# the sphere of operation of the variable
# Variable are limited to operate in certain spheres

a = 23


# global variable accessible within a local scope
def safi():
    b = 25
    print(a)


safi()

# global variable accessible within the global scope
print(a)

# INSTANCE 2
# lets create an instance were the variable is assigned twice , both inside and outside a code
# and try to access both of them by printing

a = 35


def elev():
    a = 30
    print(a)


elev()
print(a)

# let's try this instance
# where one variable is inside and another outside,


# there are four variable scopes

# built in scope
# Global scope
# Enclosing scope
# Local scope



# INSTANCE 3

# we are going to try to access a global variable , task it
# create a new local scope with similar identifier as outside the scope , task it
# and see what happens


b = "cows"


def animals():
    print(b)
    # b = "sheep"
    print(b)


animals()



# ****** GLOBAL SCOPE *****
# an scope that is accessible outside a python variable scope


# *********** BUILT IN SCOPE**********

# Accessible anywhere within the code.
# these includes the print function

# INSTANCE4
# We are going to declare a global variable
# access it within a python function but this time round declare it as global
# we are going to test if the outcome of the global variable changes

a = 45


def row():
    # global a
    a = 54
    print(a)


row()
print(a)


# the outcome is once we declare a variable is global
# this means it is accessible both inside the python function and outside it.
# thus when value is changes inside the python function it also updates to the outside function


# INSTANCE 5


def red():
    a = 1

    def blue():
        a = 2
        b = 2
        print(a)
        print(b)

    blue()
    print(a)


red()


def red():
    a = 1

    def blue():
        nonlocal a
        a = 2
        b = 2
        print(a)
        print(b)

    blue()
    print(a)

red()



# TAKE AWAY
# 1. global variables are accessible inside the local scope and global scope
# 2. Local variables are not accessible within the global scope
# 3. If you want to change the value of a global variable within a local scope,
# you first declare it as a global scope

# 4. Values that are both not locals and neither global are called non locals
# 5. If you want to change the value of a non-local you first declare it as mon local
# 6. The best practice is to pass variable as a parameter between the local and global variable.


