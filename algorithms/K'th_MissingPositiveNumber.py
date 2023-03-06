# Problem:
    # Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
    # Return the kth positive integer that is missing from this array.

# Solution 1: || Both time and space complexity is O(n) ||
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing = {}
        n = 1
        key = 1
        
        for i in arr:
            while n < i:
                missing[key] = n
                key += 1
                n += 1
            n += 1

        if k in missing:
            return missing[k]
        
        return (k + arr[-1]) - len(missing)


# Solution 2:
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr = set(arr)
        for i in range(1, 1001):
            if i not in arr and k:
                k-=1
            if i not in arr and k==0:
                return i
            
# The time complexity of this algorithm is O(n), where n is the length of the input array.
# The algorithm iterates over a range of numbers from 1 to 1000 and checks if each number is in the input array.
# Since the range is fixed at 1000, the time complexity is constant and does not depend on the value of k.
# However, in the worst case scenario where all the numbers from 1 to 1000 are missing, the algorithm will need to iterate over all 1000 numbers,
# resulting in a time complexity of O(1000) or O(1).

# The space complexity of this algorithm is also constant, as the only additional data structure used is the set representation of the
# input array, which has a size of at most n. Therefore, the space complexity of this algorithm is O(n), where n is the length of the
# input array. However, since the input array is modified in place and converted to a set, the actual space usage may be lower.
            