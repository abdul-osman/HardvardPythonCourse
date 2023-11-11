# INTEGER
# There is a no decimal point in an int

x = float(input('What is x? '))
y = float(input('What is y '))

print(round(x+y))  # this is nesting functions

"""
round(number[, ndigits])

round is the function name
number is the positional argument, it takes 1 number
the brackets are optional
ndigits specifies what nth you want to round it,
for example 10th or 100th
"""
print((round(x + y, 1)))
print((round(x + y, 2)))
print((round(x + y, 3)))
print((round(x + y, 4)))
print((round(x + y, 5)))
print((round(x + y, -1)))
print((round(x + y, -2)))
print((round(x + y, -3)))
print((round(x + y, -4)))
print((round(x + y, -5)))
print((round(x + y, 0)))

print(f"{10000000:,}") # The :, inserts commas
print(f"{10000012.123:.2f}")  # The :. specifies how many
print(f"{10000012.123: 2f}")

a = round(x + y)
b = round(x + y, 0)

if type(a) is int:
    print(a)
    print('a is an int')

else:
    print(a)
    print('a is a float')


if type(b) is int:
    print(b)
    print('b is an int')
else:
    print(b)
    print('b is a float')

print(round(7.0))
print(round(76.5))
print(round(674, 0))
print(round(674.31, 0))
print((round(674, -4)))

# end










