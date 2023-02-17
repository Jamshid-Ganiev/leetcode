# Problem:
    # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
    # The relative order of the elements may be changed. More formally, if there are k elements after removing the duplicates,
    # then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k
    # elements. !!! I can't allocate extra space for another array, i need to modeify the input array in-place.

# Solution1: 
     # My 1st brute force solution is a bit simple
def removeElement(nums: list[int], val: int) -> int:
        index = 0
        while val in nums:
            index = nums.index(val)
            nums.pop(index)
        return len(nums)

# Beats over 70% with Memory of 13.9
