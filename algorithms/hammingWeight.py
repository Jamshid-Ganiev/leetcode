# Problem:
  # Write a function that takes the binary representation of an unsigned integer and
  # returns the number of '1' bits it has (also known as the Hamming weight).

#Solution 1: | Both Time and Space comlexity is O(Log n)

def hammingWeight(n: int) -> int:
    binary = ''
    result = 0

    while n != 0:
        binary += str(n % 2)
        n = n // 2
    binary = binary[::-1]
    for i in binary:
        if int(i) != 0:
            result += 1

    return result

#Solution 2: | 
    # Time complexity is O(k), where k is the number of set bits in the input ineteger
    # Space comlexity is O(1), as the only variable used in the algorithm is 'count', which takes constant space

def hammingWeight(n: int) -> int:
    count = 0
    while n != 0:
        count += 1
        n &= n - 1
    return count
