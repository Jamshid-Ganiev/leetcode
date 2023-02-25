# Problem: 
    # A phrase is a plaindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric
    # charachters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    # Given a string s, return true if it is a palinrome, or false otherwise.

# Solution 1 | Both Time and Space complexity is O(n)

def isPalindrome(s: str) -> bool:
    if s:
        chars = ''
        for char in s:
            if char.isalnum():
                chars += char
        chars = chars.lower()
        f = 0
        b = -1
        while f <= (len(chars) - 1):
            if chars[f] != chars[b]:
                return False
            f += 1
            b -= 1
        return True
    else:
        return True

# Solution 2 | Time Complexity is still O(n), But Space complexity is optimized to O(1)

def isPalindrome(s: str) -> bool:
    if not s:
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True

# Solution 3 | Both Time and Space complexity is O(n). BUT it is so effcient when it comes to runtime.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_striped_s = [c for c in s.lower() if c.isalnum()]
        backward_striped_s = forward_striped_s[::-1]
        return forward_striped_s == backward_striped_s