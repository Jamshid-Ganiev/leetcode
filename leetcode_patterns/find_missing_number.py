# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1 + 2 + 3 = 6. n * (n + 1) / 2
        # 1 + 2 + 3 + 4 = 4*(4+1) / 2 = 20 / 2 = 10 
        # length. n*(n+1)/2
        n = len(nums)
        total = n*(n+1)//2
        for num in nums:
            total -= num
        return total