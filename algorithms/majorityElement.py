# Problem:
  # Given an array nums of size n, return the majority element.
  # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
  # always exists in the array.

# Solution 1: | Time complexity is O(n), and Space Complexity is O(1). 
# Using the Boyer-Moore Voting Algorithm to find most frequent integer in a given array.

def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    if nums.count(candidate) > len(nums) / 2:
        return candidate
    else:
        return None

