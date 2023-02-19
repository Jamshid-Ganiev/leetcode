# Problem: | Plus One
    # I was given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
    # the digits are ordered from most significant to least significant in left-to-right order.
    # The large integer does not contain any leading 0's.
    # So My program has to return the resulting array of digits by incrementing the large integer by one.

# Solution 1: | My Brute force/first solution | Time and Space comlexity are both O(n)

def plusOne(digits: list[int]) -> list[int]:
        n = -1
        digits[n] += 1
        while n >= -len(digits) and digits[n] % 10 == 0:
            digits[n] = 0
            n -= 1
            if n >= -len(digits):
                digits[n] += 1
            else:
                digits.insert(0, 1)
        return digits

# Solution 2: | My Brute force/first solution |
#             |  Time complexity is O(n) | Space complexity is O(1) this time

def plusOne(digits: list[int]) -> list[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            if carry == 0:
                break
            total = digits[i] + carry
            digits[i] = total % 10
            # in this case enev if carry is equal to 0.9, the // operator assign 0
            carry = total // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
