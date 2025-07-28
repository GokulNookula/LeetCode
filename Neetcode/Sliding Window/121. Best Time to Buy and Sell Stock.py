# OPTIMAL Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is because time moves to the right not behind
        # Buying stock Low on day 1
        l = 0
        # Selling stock High on day 2
        r = 1
        maxProfit = 0

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
We know that time only moves with the days increasing thus by this we should know that we need to use two pointers.
Thus we first set left pointer as 0th element aka day 1 in the array and right to the day 2 of the array. Now we
keep iterating over the array while our right pointer is less than the length of the price array, aka the end of trading
days data. For the if statement we know that we only go into it if we buy low aka left is less and we sell high aka
right is greater than left. So when we go in we need to calculate the profit for those days. Next once we do we need to
make sure that if our current profit we calculated is greater than our maxProfit. If it is then we update it or else 
we just move our right pointer by +1. Else if we are buying high or buying at the same price as sell price being low or
equal to buy price then we update our left pointer to our current right pointer as we want to buy at the lowest price
and then we increase the right pointer by +1. Thus by handling it this way we are only iterating over the array once
and we do not use any arrays to store the profit calculated thus making it O(1).
'''


# My Solution with AI - OPTIMAL on 3/26/2025
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for sell in prices:
            minPrice = min(minPrice, price)
            profit = sell - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
'''Explained: Time Complexity: O(n) Space Complexity: O(1)
This uses dynamic programming to also calculate the profit while focusing on finding the minimum price for buying 
stored while we iterate over for all the sell prices in the array and then only store the one that gives us the most profit
'''

# My solution - close to Optimal Solution on 4/5/2025
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = prices[0]
        maxProf = 0

        for right in prices:
            maxProf = max(maxProf, (right - left))
            if right <= left:
                left = right
        return maxProf

# My solution - OPTIMAL on 6/9/2025
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left  = 0
        right = 1

        maxProfit = 0

        while(right < len(prices)):
            
            profit = prices[right] - prices[left]

            if profit > maxProfit:
                maxProfit = profit

            if prices[right] < prices[left]:
                left = right

            right += 1
        return maxProfit

# My solution - Almost solved it on 7/27/2025
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        maxProfit = 0

        while (right < len(prices)):

            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
