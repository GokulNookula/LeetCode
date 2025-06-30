# OPTIMAL Solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Initalizing the hare and tortorise method
        slow = 0
        fast = 0

        # First part of the algorithm to set the hare and tortorise method
        # of checking if there is a cycle in the list
        while True:
            # Moving the pointers to the next one to start the checking
            slow = nums[slow]
            # Basically we are taking the current number of the fast pointer
            # and we are using it as the next index to move twice basically
            fast = nums[nums[fast]]
            # Condition to check if there is a cycle in the list
            if slow == fast:
                break
        # Part two of the algorithm as we want to get both the slow pointers
        # to point to the same value
        slow2 = 0
        while True:
            # Moving the pointers to the next one to startthe checking
            slow = nums[slow]
            slow2 = nums[slow2]
            # Both of them meet then we got the cycle index
            if slow == slow2:
                # Returning the number since we found it
                return slow
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''

# My Solution - not Optimal on 6/29/2025
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1
