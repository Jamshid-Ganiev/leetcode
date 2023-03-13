# Problem:
  # Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
  # You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
  # You must also not convert the inputs to integers directly.

# Solution 1: Time complexity is O(n), Memory Complexity is O(1)
  # The first Brute Force Solution came to mind: || Time spent: 5-10 mins

def addStrings(num1: str, num2: str) -> str:
    nums = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    result = 0
    l = 1
    for i in num1[::-1]:
        result += (nums[i] * l)
        l = l * 10
    
    l = 1
    for i in num2[::-1]:
        result += (nums[i] * l)
        l = l * 10

    return str(result)

# 1. Define a dictionary nums that maps each digit character to its corresponding integer value.
# 2. Initialize a variable result to 0.
# 3. Initialize a variable l to 1.
# 4. Iterate through the characters of num1 in reverse order:
#     a. Use the nums dictionary to look up the integer value of the current digit.
#     b. Multiply the integer value by l.
#     c. Add the result to the product.
#     d. Multiply l by 10.
# 5. Initialize a variable l2 to 1.
# 6. Iterate through the characters of num2 in reverse order:
#     a. Use the nums dictionary to look up the integer value of the current digit.
#     b. Multiply the integer value by l2.
#     c. Add the result to the product.
#     d. Multiply l2 by 10.
# 7. Return the result as a string.


# Solution 2: Both T.C and M.C is O(1)
def addStrings(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))