# OPTIMAL Solution
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initalizing binary search pointers
        left = 1
        right = max(piles)
        # Initalize result to the maximum pile as that is the last number we
        # get for the minimum result
        minRes = right

        # Iterating over the binary search to find a speed aka k 
        # the minimum value for speed of number of bananas that koko
        # can eat in the given hours
        while (left <= right):
            # Finding the midpoint aka the speed in the array that
            # changes based on the minRes of we get from piles on
            # how long aka hours it takes to eat those piles and
            # whether if we can finish it in given h
            k = (left + right) // 2

            # Initalizing the number of hours it will take for
            # the above speed we obtained aka k
            hours = 0

            # Iterating through each pile based on the speed to find
            # the hours needed to eat that pile
            for p in piles:
                # Adding the hours of each pile to get the total
                # we use .ciel to round it up
                hours += math.ceil(float(p) / k)

            # Checking if the above hours for that speed is less than
            # h aka total hours before the guard returns
            if hours <= h:
                # Updating min result if our new speed value is less than
                # our old speed value as we did meet the hours condition above
                minRes = min(minRes, k)
                # Updating right pointer and doing - 1 to not iterate over
                # the same pointer again
                right = k - 1
            else:
                # Updating right pointer and doing - 1 to not iterate over
                # the same pointer again
                left = k + 1
        # Smallest speed returned to eat most banana's in the given hours
        return minRes
'''Explained: Time Complexity: O(n log n) and Space Complexity: O(1)
'''
