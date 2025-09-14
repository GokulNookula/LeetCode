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
            # Moving the pointers to the next one to start the checking
            slow = nums[slow]
            slow2 = nums[slow2]
            # Both of them meet then we got the cycle index
            if slow == slow2:
                # Returning the number since we found it
                return slow
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
In this problem since we are trying to find a duplicate in a list. This is similar to the Hare and Tortoise
aka Floyd Cycle Algorithm. First we need to check if there is even a loop in our list. We do this by
setting a slow and fast pointer and start a while loop and check basically where slow pointer moves based on
1 point at a time and the fast pointer moves based on the number in that index thus moving by more than 1 aka 
n number of steps and according to Floyd's algorithm if there is a cycle these pointers will meet no matter what
once we find that we break out of the first loop else we just return nothing. If there is a loop then we keep track 
of our first slow pointer and create a slow2 pointer which starts from the beginning for initializing and we 
continue to iterate by checking based on the previous pointer number we got inside by only being the pointer by 1 move
since slow pointer is already in the loop it shouldn't go anywhere and we are just waiting for slow2 pointer to enter that
loop. Once we find that slow and slow2 pointer are equal which means there is a duplicate number then we return the answer or 
else we return nothing.
'''

# My Solution - not Optimal on 6/29/2025
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

# My solution - OPTIMAL on 7/13/2025
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        return None

# My solution - OPTIMAL on 7/29/2025
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                break
        return slow

# My solution - OPTIMAL on 9/13/2025
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
        return slow
