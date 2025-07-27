# OPTIMAL Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        resMaxArea = 0
        l = 0
        r = len(height) - 1

        while (l < r):
            area = (r - l) * min(height[l], height[r])
            resMaxArea = max(resMaxArea, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                # When both the pointers are the same height
                # You can either decrement right pointer or increment left
                r -= 1
        return resMaxArea

'''
Explained: Time Complexity: O(n) Space Complexity: O(1)

We basically use the two pointer method where we make a while loop and have a condition
where left must be less than right. To calculate the area of a rectangle it is width * height
so basically (r - l) REMEMBER r and l are indexes so thus you have to do that to get the width. Then
we finally find the smallest between left height and right height as that is how much we can fill up
even if one of them is bigger. Once we get the number we check if our new area is greater than our old 
resMaxArea and if it is we update it or else we don't. Then we pretty much move the left pointer if the height
of the left line is less than the right height line by incremeting the left pointer or else we decrement the right pointer
if the height of the right line is less than the left height line. We also have to deal with another condition where
both are the same then you can either decrement right or increment left. Then we finally return the maxArea.
'''

# My solution - OPTIMAL on 3/25/2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = float(-inf)

        while(left < right):

            area =  (right - left) * min(height[left],height[right])
            maxArea = max(maxArea,area)
            if height[left] < height[right]:
                left += 1
            else:
                # When both the pointers are the same height
                # You can either decrement right pointer or increment left
                right -= 1
        return maxArea

# My solution - OPTIMAL on 3/31/2025
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        maxArea = float(-inf)

        while (left < right):
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area,maxArea)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

# My solution - OPTIMAL on 6/11/2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = float("-inf")

        while (left < right):
            area = (right - left) * min(height[left], height[right])

            if area > maxArea:
                maxArea = area
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea

# My solution - OPTIMAL on 7/20/2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxArea = float("-inf")

        while (left < right):
            # Wdith * height
            area = (right - left) * min(height[left], height[right])

            if area > maxArea:
                maxArea = area

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

# My solution - OPTIMAL on 7/26/2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right  = len(height) - 1
        maxArea = float("-inf")

        while (left < right):
            area = (right - left) * min(height[left], height[right])

            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
