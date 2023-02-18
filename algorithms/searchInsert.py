# Problem:
    # Given aa sorted array of distinct integers and a target value, the program should return the index if the target is found.
    # If not, it should return the index where it would be inserted in order.
    # An algorithm with O(log n) time complexity should be used.

# Solution: || I used Modified Binary Search Algorithm as its time complexity is O(log n)

def searchInsert(nums: list[int], target: int) -> int:
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                
                if target == nums[mid]:
                    # target found, return index
                    return mid
                elif target < nums[mid]:
                    # get rid of the right half
                    end = mid - 1
                else:
                    #get rid of the left half
                    start = mid + 1
            return start