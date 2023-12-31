"""
a = "meow"
i = 0
while i < 5:
    print(a)
    i+=1



print("meow" * 3)
print("woof\n" * 3)
print("quak\n" * 3, end="")

def main():
    number = get_number()
    meow(number)

"""

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        

def meow(n):
    for _ in range(n):
        print("meow")


main()