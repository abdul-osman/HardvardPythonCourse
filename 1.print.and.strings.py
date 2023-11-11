# FUNCTIONS:
# Function is like an action or a verb
# that lets you do something in the programme.
# Python comes with predetermined functions, but you can also make your own.
# For example print() is a function.

print()

# ARGUMENTS:
# An argument is an input to a Function that somehow influences its behaviour.
# You pass arguments to Functions, Functions take in parameters.
# In below example Helllo World is the argument.

print('Hello World')

# SyntaxError is usually a keyboard mistake.
# Variable is a container for a value.
# Functions can have return values.
# Please note below, single equal sign means assignment.

name = input('What is your name? ')
print('Hello ' + name)

# Instead of + you can use a comma to add multiple arguments.
# Notice when you use a comma you will get an extra space.

print('Hello ', name, name)

# the backslash is called an Escape character, it has good uses.
# The default for end is \n which means new line

print('Hello, ', end="")
print(name)

# Use the backslash to add quotes inside the string.

print("Hello \"Friends\"")

# F string or Format string

print(f"Hello {name}")

# The str data type has many useful built-in METHODS.
# Some of these are:

print(name)
print(name.strip())  # strip() method removes white space before and after.
print(name.capitalize())  # Only capitalises the first word.
print(name.title())  # Capitalises all letters.
print(name.strip().capitalize())  # Concatenate methods on one line.

# Final:

name = input("What is your name? ").strip().title()
print(name)

# Split user's name into first name and last name
first, last = name.split(" ")
print(first)
print(last)
