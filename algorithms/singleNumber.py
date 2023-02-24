# Problem:
    # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    # My program should run in O(n) Time complexity and Space complexity with O(1)

# Solution 1:| Space and Time complexity are both O(n)
def singleNumber(nums: list[int]) -> int:
    l = {}
    for num in nums:
        if num not in l:
            l[num] = 0
        l[num] += 1
    result = min(l, key = l.get)
    return result
        
# Solution 2:| Time complexity is O(n), and Space complexity is O(1)| Using bitwise operator

def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

