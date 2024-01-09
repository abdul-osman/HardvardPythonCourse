"""
Sys: 
This module provides access to some variables 
used or maintained by the interpreter 
and to functions that interact strongly with 
the interpreter. 
It is always available

sys.argv, argument vector, the list of all
the words the human typed in at the prompt
before they hit enter.
"""

import sys

"""
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments.")
else:
    print("Hello, my name is", sys.argv[1])
"""

# The above more simplified:
"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

print("Hello, my name is", sys.argv[1])
"""

# Slices: a subset of a data structure like a list

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)





