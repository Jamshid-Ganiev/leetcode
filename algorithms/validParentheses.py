# Description:
#     Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Solution1: The 1st brute force solution came to my mind:
    # When I was doing smth else (not coding or even studying), solution came to my mind spontaneously. Then I opened my laptop
    # write the code and checked. Results: R: beats 82.39% with 30ms. M: 13.9 
def isValid(s: str) -> bool:
    openings = ['[', '{','(']
    closings = [']', '}',')']

    if len(s) % 2 == 1 or s[0] in closings or s[-1] in openings:
        return False

    brackets = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    s_list = list(s)
    half = []
    while s_list:
        char = s_list[0]
        if char in openings:
            val = brackets[char]
            half.append(val)
            s_list.pop(0)
        if char in closings:
            if half:
                if char == half[-1]:
                    half.pop()
                    s_list.pop(0)
                else:
                    return False
            else:
                return False
    if half:
        return False
    return True