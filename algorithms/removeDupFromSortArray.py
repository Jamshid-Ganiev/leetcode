# Problem: 
    # A sroted array (in a non-decreasing order) with duplicates is given, the problem is
    # all dulicates should be removed but the length of the list should stay the same.
    # no matter what you add to the list as long ass the length of the list is the same as it was given

# Solution 1: The 1st solution came to my mind(in around 20 mins) is that creating two variables,
#  one is called temp(=0), and the other is called(sign='_'),using while loop I store the first elementof the list
#  in temp, if the next element is equal to the temp, that item will be popped from the list by using its index, and sign
#  variable is appended to the list, if the sign comes in the loop, it breaks and return the length of the list as a result.

def removeDuplicates(nums: list[int]) -> int:
    length = len(set(nums))
    if length != len(nums):
        temp = 0
        sign = '_'

        index = 0
        while temp != sign:
            num = nums[index]

            if index != 0 and num == temp:
                nums.append(sign)
                nums.pop(index)
            else:
                index += 1
            
            temp = num
            
        index = index - 1 
        return index
    
    return length
# Results: A bit disappointing with R:205ms | My:15.7

