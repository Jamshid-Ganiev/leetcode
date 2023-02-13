# Problem: 
    # Given an "integer" x, return true if x is a palindrome, and false otherwise
#Eplanation:
    # A palindrome is a word, phrase, numbers, pr other sequence of characters which reads the same backward or forward.
    # in this case, only an integer
#Example: 
    # Input: x = 121
    # Output: true

    # Input: x = -121
    # Output: false

#Solution1: || the 1st solution came to my mind
def isPalindrome(x: int) -> bool:
    if x >= 0:
        xr = ''
        for ch in list(reversed(str(x))):
            xr += ch

        if x - int(xr) == 0:
            return True
        return False
    else:
        return False
    
print(isPalindrome(1010))

# Accapted!
#Runtime: 55ms
#Beats: 88.97%
#memory: 14 || :(

#Solution2: || One-Line code:
def isPalindrome2(x: int) -> bool:
    return False if x < 0 else x == int(str(x)[::-1])


print(isPalindrome2(110))

# Accapted!
#Runtime: 62ms
#Beats: 71.15%
#memory: 13.9 || :(

# Solution 3: || Algorithmic way
def isPalindrome(x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
	
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
            
        return True if (x == result or x == result // 10) else False

# Accapted!
#Runtime: 54ms
#Beats: 90.52%
#memory: 13.9 || :)