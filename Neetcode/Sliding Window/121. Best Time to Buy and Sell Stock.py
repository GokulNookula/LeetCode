# OPTIMAL Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is because time moves to the right not behind
        # Buying stock Low on day 1
        l = 0
        # Selling stock High on day 2
        r = 1
        maxProfit

        # To make sure we do not go out of bound of prices
        while r < len(prices):
            
            # If we are buying low and selling high aka left less than right
            if prices[l] < prices[r]:
                # Then we calculate how much profit we made
                profit = prices[r] - prices[l]
                # Then we have to check if our current 
                # profit is greater than maxProfit
                maxProfit = max(maxProfit, profit)
            # If we are buying high ad selling low 
            # or buying and selling at the same price
            else:
                # We set the left pointer to the current right pointer
                # Later we update it
                l = r
            # We need to move to the next iteration of the array since
            # Our condition was not met
            r += 1
        return maxProfit

'''Explained: Time Complexity: O(n) Space Complexity: O(1)

'''


# My Solution - Not Optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit

