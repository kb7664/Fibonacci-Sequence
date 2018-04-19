##############################
#   Fibinacci Sequence
#
#   Author: Karim Boyd
##############################

# This program demonstrates one of the many ways to build the Fibonacci 
# sequence using recursion and memoization

# First import lru_cache to store the results of previous runs to 
# memory
from functools import lru_cache
# Set the dictionary to hold upto 1000 items in cache
@lru_cache(maxsize = 1000)
# Set up Fibinacci function
def fibonacci(n): 
    if n == 1:
        return 1
    elif n == 2: 
        return 1
    elif n > 2: 
        return fibonacci(n-1) + fibonacci(n-2) 
# Test the function
for n in range (1, 101): 
    print(n, " : ", fibonacci(n))