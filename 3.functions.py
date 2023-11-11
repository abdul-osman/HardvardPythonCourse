"""
FUNCTIONS
Define/create a function by def keyword

if you are going to use a function it must
already exist, i.e. must be above in code

You should create a main function
then define your functions
then call main at the bottom
this will eliminate the above problem.

Scope problems, scope refers to
a variable only existing in the context
in which you defined it
"""

name = input("What is your name? ")


def hello(a="john doe"):  # John Doe is a placeholder incase user doesn't enter a name.
    print(f"Hello {a}")


hello(name)
hello()

"""
The code below, we use a function to
return a value
"""


def main2():
    x = int(input('What is x? '))
    print("X squared is", squared(x))


def squared(a):
    return a * a


main2()
