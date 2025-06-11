# OPTIMAL Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initalizing two pointers for binary search
        left = 0
        right = len(nums) - 1
        
        # We stopping iterating if we cross over our left and right pointer
        # This means we have went through the entire array
        while (left <= right):
            # To prevent overflow we do right - left pointer as adding them
            # can cause us to overflow when finding the midpoint of the array
            midpoint = ((right - left) // 2) + left

            # Checking if our answer is less than target
            if (nums[midpoint] < target):
                # We update left to our current midpoint and add 1
                # as we already have visited that number so we add to skip it
                left = midpoint + 1
            # Checking if our answer is greater than target
            elif (nums[midpoint] > target):
                # We update right to our current midpoint and subtract 1
                # as we already have visited that number so we add to skip it
                right = midpoint - 1
            # If our midpoint is the same as target then we return
            else:
                return midpoint
        # If we crossed over the pointer then we didnt find anything
        # thus we return -1
        return -1

'''Explained: Time Complexity: O(log n) Space Complexity:  O(1)
FILL THIS OUT ON THURSDAY
'''


# My solution - 6/10/2025
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            midpoint = ((right - left) // 2) + left

            if (nums[midpoint] < target):
                left = midpoint + 1
            elif (nums[midpoint] > target):
                right = midpoint - 1
            else:
                return midpoint
        return -1
