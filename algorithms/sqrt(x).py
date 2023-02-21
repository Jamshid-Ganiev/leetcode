# Problem:
    # Given a non-integer x, return the square root of x rounded down to the nearest integer,
    # The returned integer should be non-negative as well.
    # ANY BUILT-IN exponent function or operator must not be used.
    # For example, pow(x, 0.5) in c++ or x**0.5 in python


# Solution 1: | Without using any buil-in function or operators
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    i = 1
    temp = i * i
    while x >= temp:
        i += 1
        temp = i * i
    return i - 1

# Solutions using math python library | Both Memory and Time Efficient
# Solution 2:
import math
def mySqrt(x: int) -> int:
    return math.floor(math.sqrt(x))


# Solution 3:
import math
def mySqrt(x: int) -> int:
    return int(abs(math.sqrt(x)))