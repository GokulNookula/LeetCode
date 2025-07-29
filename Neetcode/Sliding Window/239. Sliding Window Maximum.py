# OPTIMAL Solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Contain the max ouput for each windows
        output = []
        # Initalizing a monotonic decreasing order of a queue aka dequeue
        # It contains Indexes of the element
        queue = deque()
        # Intialize the pointers for the windows
        l = r = 0

        while r < len(nums):
            # We check if our queue is not empty and the top most value
            # of the queue is less than the right pointer value we are adding
            # aka we pop smaller values from the queue
            while queue and nums[queue[-1]] < nums[r]:
                # popping the small values
                queue.pop()
            # Appending the new value after popping all the smaller values
            # that are smaller than the current right pointer value
            queue.append(r)

            # Removing left values from the window aka if it is out of bound
            # then we need to remove it to preserve the window size
            if l > queue[0]:
                # Popping the left side of the queue
                queue.popleft()

            # Checking our size of our window as the right pointer
            # must be atleast the size of k window since we initalized
            # right as 0
            if (r + 1) >= k:
                # Appending the left most value of the queue as it
                # is the maximum number because monotonic dqueue
                output.append(nums[queue[0]])
                # Only if our above condition of right pointer is true then
                # we increment left pointer
                l += 1
            # Updating right pointer
            r += 1
        return output
'''Explained: Time Complexity: O(n) Space Complexity: O(n)
'''
# My solution - Did not solve it on 7/28/2025
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        resMaxEachWindow = []
        queue = deque()

        left = 0
        right = 0

        while(right < len(nums)):

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if ((right - left)+ 1) >= k:
                resMaxEachWindow.append(nums[queue[0]])
                left += 1
            right += 1
        
        return resMaxEachWindow
