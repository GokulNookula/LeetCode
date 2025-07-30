# OPTIMAL Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initalizing a value to store as 0
        # because XORing anything with 0 is always
        # going to return the number itself
        res = 0

        # Iterating through the entire nums array
        for n in nums:
            # We basically XOR each number until the
            # end however if we have even number of 1's
            # or 0's those cancel out due to XOR logic
            res = res ^ n
        # Returning the single number that was found
        return res
'''Explained: Time Complexity: O(n) Space Complexity: O(1)
'''
