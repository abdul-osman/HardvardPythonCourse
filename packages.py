"""
Packages are 3rd party libraries.

PyPi is a popular
website for python packages.

Pip is a package manager used to install packages
from the command line.
"""

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
else:
    print("error")



