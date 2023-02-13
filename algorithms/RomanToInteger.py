# Explanation: 
    # Roman numerals are represented by seven different symbols: I, V, X, L. C, D and M
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000

# Problem: 
    # Given a roman numeral, covert it to an integer
    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3

# Solution 1: The 1st solution came to my mind. 
#           | BEATS 98.29% | runtime: 36ms | M:13.8
def romanToInt(s: str) -> int:
    roman_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    result = 0
    temp = 0
    for char in list(reversed(s)):
        num = roman_dict[char]
        if num >= temp:
            result += num
        else:
            result -= num
        temp = num

    return result

print(romanToInt("MCMXCIV"))

# Just Smashed