# Problem:
    # I am climbing a staircase. It takes n steps to reach the top.
    # Each time I can climb either 1 or 2 steps. I should find how many distinct ways I can have to climb to the top.
    # Constraints: 1 <= n <= 45

# Solution 1: | Fibonacci sequence is a clear solution for this:| using for loop
def climbStairs(n: int) -> int:
        x = y = 1
        for _ in range(n):
            x, y = y, x + y
        return x

# Solution 2: using recursion and @lru_cache decorator
from functools import lru_cache
class Solution:
    @lru_cache
    def climbStairs(n: int) -> int:
        if n < 2:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)