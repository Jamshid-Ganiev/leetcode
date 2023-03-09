# Problem:
  # Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
  # Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from
  # that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
  # Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    # Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4


# Solution :
# The time complexity of this solution is O(n log m)
# The space complexity is O(1)

def minEatingSpeed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)

    def canEatAllWithin(piles, k, h):
        total_time = 0
        for pile in piles:
            total_time += (pile - 1) // k + 1
        return total_time <= h

    while left < right:

        mid = (left + right) // 2
        
        if canEatAllWithin(piles, mid, h):
            right = mid
        else:
            left = mid + 1

    return left