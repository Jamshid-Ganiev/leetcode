# Problem:
  # Given an integer array nums, return true if any value appears at least twice in the array, 
  # and return false if every element is distinct.

# Solution 1: | Both Time and Space Complexity is O(n)

def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

