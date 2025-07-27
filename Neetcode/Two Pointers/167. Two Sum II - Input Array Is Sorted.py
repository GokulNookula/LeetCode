# My solution - OPTIMAL Solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while (left < right):

            if (numbers[left] + numbers[right] > target):
                right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                return [left+1,right+1]

'''
Explained: Time Complexity: O(n) Space Complexity: O(1)

In the question we know that the array is arranged in the ascending order. (Hint 1 for Two Pointer)
We also notice that we need to solve the problem with no space allocated. (Hint 2 for Two Pointer)
Thus based on these information we can concurr that we need to use two pointers where
we make a while loop and we check if we are over the target number then we decrement our right pointer
and if we are less than our target number then we increase our left pointer. Do this process
until we reach our goal and thus we return it.
'''

# Optimal Solution Obtained again on 3/5/2025
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while(left  < right):

            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1,right + 1]
        return [-1,-1]

# My solution - OPTIMAL on 3/25/2025
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while (left < right):
            total = numbers[left] + numbers[right]

            if (total < target):
                left += 1
            elif (total > target):
                right -= 1
            elif (total == target):
                return [left + 1, right + 1]
            else:
                return [-1,-1]

# My solution - OPTIMAL on 7/20/2025
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while (left < right):
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            elif total == target:
                return [left + 1, right + 1]
        return [-1,-1]

# My solution - OPTIMAL on 7/26/2025
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while (left < right):
            total  = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            elif total == target:
                return [left + 1,right + 1]
        return [-1,-1]
