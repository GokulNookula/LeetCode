# OPTIMAL Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        index = 0

        for n in nums:
            index = index ^ n
        return index
'''Explained: Time Complexity: O(n) Space Complexity: O(1)
'''
