# Problem: Best time to but and sell stock
    # Given an array prices where prices[i] is the price of a gicen stock on the ith day. I want to maximize my profit by hcoosing a single day
    # to buy one stock and choosing a different day in the future to sell that stock. My program should return the max profit I can achieve
    # from this transaction. If I cannot achieve any profit, 0 should be returned.

# Solution 1: |Using a for loop
def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
     
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit
    return max_profit

# Time and Space Complexity
  # The time complexity of this solution is O(n), where n is the length of the input array. This is because we are looping through
  # the array only once.

  # The space complexity of this solution is O(1), which means it uses a constant amount of extra space.
  #  This is because we are only using a fixed number of variables ("min_price" and "max_profit") to keep track of the minimum
  #  price and maximum profit, and we are not creating any new data structures that depend on the size of the input array.
