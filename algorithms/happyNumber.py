# Problem:
    # Write an algorithm to determine if a number n is happy.

    # A happy number is a number defined by the following process:
    # Starting with any positive integer, replace the number by the sum of the squares of its digits.
    # Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    # Those numbers for which this process ends in 1 are happy.
    # Return true if n is a happy number, and false if not.

# Solution 1:
def isHappy(n: int) -> bool:
    def recursion(n, seen):
        if n in seen:
            return False
        seen.add(n)
        result = 0
        while n > 0:
            digit = n % 10
            result += digit ** 2
            n //= 10
        if result == 1:
            return True
        return recursion(result, seen)
    return recursion(n, set())
