import sayings
import sys

if len(sys.argv) == 2:
    sayings.hello(sys.argv[1])
    sayings.goodbye(sys.argv[1])
    
# Cleaner:
    
from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
