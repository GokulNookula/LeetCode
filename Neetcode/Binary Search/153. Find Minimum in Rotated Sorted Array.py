# OPTIMAL Solution
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left  = 0
        right = len(nums) - 1

        while (left < right):
            midpoint = left + ((right - left) // 2)

            if nums[midpoint] < nums[right]:
                right = midpoint
            else:
                left = midpoint + 1
        return nums[left]
'''Explained: Time Complexity: O(log n) and Space Complexity: O(1)
'''
