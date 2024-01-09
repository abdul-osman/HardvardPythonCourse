"""
Libaries are generally files of codes that other people
have written that you can use your in program

Modules is a library that has one or more functions or features
that have built into it. Used for reusability.
"""


import random


coin = ["Heads", "Tail"]
teams = ["Arsenal", "Chelsea", "Liverpool", "Spurs"]
choice = "Heads"
print(random.choice(coin))
print(random.randint(1,10))
random.shuffle(teams)
print(teams)
for team in teams:
    print(team)


import statistics

a = statistics.mean([100, 90, 90])
print(a)



