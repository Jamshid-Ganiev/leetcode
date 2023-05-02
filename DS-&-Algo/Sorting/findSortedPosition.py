# Modified version of the binary saerch that returns the index within a sorted list sequence indicating where the target should be located.

# Algorithm:
def findSortedPosition(the_list, target):
    low = 0
    high = len(the_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if the_list[mid] == target:
            return mid
        elif target < the_list[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return low

nums = [2,5,10,13,18,20,23,30,50,80,99]
target = 25
print(nums)
position = findSortedPosition(nums, target)
nums.insert(position, target)
print(nums)


# result
# >> [2, 5, 10, 13, 18, 20, 23, 30, 50, 80, 99]
# >> [2, 5, 10, 13, 18, 20, 23, 25, 30, 50, 80, 99]