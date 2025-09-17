class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # Initalize a stack that contains the height and the index aka 
        # it is a pair
        stack = []

        # For loop that keeps track of index and height of current variable
        for index, height in enumerate(heights):
            # Storing the index before we add it to the stack
            # to use it for the smallest height value of stack start
            # in order to be able to extend it backwards
            start = index

            # While our stack is not empty and the top value in the stack
            # and the top value's height is greater than the height we 
            # just reached then we need to pop
            while stack and stack[-1][1] > height:
                # Popping because the above condition was true
                i, h = stack.pop()
                # Checking if our popped height is the max
                # area of the rectangle
                # (i - index - current height) is the width
                maxArea = max(maxArea, h * (index - i))
                # Extending our start index backwards to the index we
                # just popped
                start = i
            # Adding the pair back into the stack after updating
            stack.append((start, height))
        
        # To compute the heights of remaning ones in the stack of the
        # extended ones in the histogram of heights
        for index, height in stack:
            # Update our max area stored by finding the max between maxArea
            # and computing the new area which is height stored in the stack
            # times width aka length of histogram minus the current index stored
            # in the stack
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea
'''Explained: Time Complexity: O(n) and Space Complexity: O(n)
'''

# My solution - Didnt solve it on 7/28/2025
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = 0
        stack = []
        maxArea = float("-infinity")
        start = 0

        for index, height in enumerate(heights):

            start = index

            while stack and stack[-1][1] > height:
                i, h = stack.pop()

                maxArea = max(maxArea, h * (index - i))
                start = i
            stack.append((start,height))
        
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea

# My solution - Didnt' solve it on 9/16/2025
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = float("-infinity")
        start = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()

                maxArea = max(maxArea, h * (index - i))
                start = i
            stack.append((start,height))
        
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea
