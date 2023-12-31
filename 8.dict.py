""" 
dict or dictionaries are data structues that
allow you to associate one value wit
another value.
keys and values.
"""
"""
students = {
    "Ali": "London", 
    "Jason": "Manchester",
    "Emily": "Luton",
    }

for student in students:
    # print(f"{student}: ", students[student])
    print(f"{student}: ", students[student], sep="")

"""
students = [
    {"name": "Ali", "city": "London", "gender": "male"},
    {"name": "Jason", "city": "Manchester", "gender": "male"},
    {"name": "Emily", "city": "Luton", "gender": "female"},
    {"name": "Ron", "city": "Bristol", "gender": None},
]

for student in students:
    print(student["name"], student["city"], student["gender"], sep =", ")