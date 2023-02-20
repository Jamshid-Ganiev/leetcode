# Problem:
    # Given two binary strings a and b, I should write a program that returns their sume as a binary string

# Solution 1: | Time complexity O(n), Space complexity O(n)
def addBinary(a: str, b: str) -> str:
    # takes the maximum length between two strings(a and b)
    max_len = max(len(a), len(b))

    # fills with zeros in front of the string according to max_len
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0

    # iterates over the string a in reverse order
    for i in range(len(a)-1, -1, -1):
        # add two binary numbers and assigns it to the sum variable
        sum = int(a[i]) + int(b[i]) + carry
        # sum % 2 returns the remainder. | 3 or 2 -> 1, carry -> 1 | 1 -> 1, carry -> 0 | 0 -> 0, carry -> 0  
        result += str(sum % 2)
        carry = sum // 2
    # if carry is 1, it adds 1 to the result, else nothing happens
    if carry:
        result += str(carry)
    #return the reverse of the string using string slicing
    return result[::-1] 

#The time complexity of the addBinary() function is O(n), where n is the maximum length of the input strings a and b.
#This is because the function iterates over the input strings once in reverse order, performing constant time operations
#(such as addition and modulo) on each character.

#The space complexity of the function is also O(n), as the function creates new strings of length max_len (where max_len is
#the length of the longer input string), and a string result of length at most max_len + 1 (if there is a carry in the last 
# addition).

#The function could potentially use less space if it operated directly on the input strings rather than creating new strings,
#but it would also need to handle the case where one input string is shorter than the other. Overall, the current implementation
#strikes a good balance between time and space complexity.