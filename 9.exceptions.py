"""
try:
    x = int(input('Age? '))
    print(x) 
except ValueError:
    try:
        print(x)
    except NameError:
        print('n')
    """

"""
def main():
    x = get_number()

def get_number():
    while True:
        try:
            x = int(input('Age? '))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
"""
"""
def main():
    x = get_number()
    print(f"x is {x}")

def get_number():
    while True:
        try:
            return int(input('Age?? '))
        except ValueError:
            pass


main()
"""
def main():
    x = get_number("What's x? ")
    print(f"x is {x}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()