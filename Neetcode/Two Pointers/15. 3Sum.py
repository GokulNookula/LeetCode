# OPTIMAL Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

'''
Explained: Time Complexity: O(n^2) Space Complexity: O(1) or O(n) depends on the sort algorithm used

We basically make an array to hold our result of 3Sums. We first sort the array to try get all the duplicates
besides each other thus eliminating the repetitive solution adding to the result array.Then we make a for loop
to iterate with the index i and value a. Then we check if a is greater than 0 then we want to skip that element as
summing that number would not be equal to 0 thus ignoring large numbers. Then we check for duplicates by having an if 
statement to check if I > 0 and to make sure that the previous number is not the same as our current number. If it is then
we skip the loop. Once we finally get the a number we use two pointers to get the next two numbers. We now make a while loop
and make sure l less than r index pointer. Then we add up the sum of it. Then we check if our total is greater than 0 then
we decrement our right pointer as we have sorted our list in ascending order. Or if our Sum is less than 0 then we increment our
left pointer. Then if we get the answer we append it to our result array and we move our left and right pointer. Then after that
we want to make sure our new left pointer is not a duplicate again so we make sure our current left pointer is not the same as
previous left pointer and also if our left index is less than our right index. If they are the same then we increment our left pointer.
Finally we get our result and return it. Thus solution
'''


# My Solution is not Optimal

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:  # Skip duplicate elements for k
                continue
            left = k + 1
            right = len(nums) - 1    
            while (left < right):
                total = nums[k] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[k],nums[left],nums[right]])
                    
                    # Move the pointer to skip the duplicates
                    left += 1
                    right -= 1

                    # Skip duplicate values for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicate values for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

'''
Explained: Time Complexity: O(n^2) Space Complexity: O(1)

We first make an array to store all the results and also sort all the numbers in ascending order. 
Then we make a for loop and set one of the values as k. If k is greater than 0 and the current number 
is the same as the previous number, we skip it to avoid duplicates. Then, we set two pointers: left as k + 1 
and right as the last index of the array. We use a while loop to iterate over the array. If the sum of 
nums[k], nums[left], and nums[right] is less than 0, we increase left to get a bigger number. If the sum 
is greater than 0, we decrease right to get a smaller number. If the sum is 0, we add it to the result array 
and move both pointers to check for more possible solutions. Then, we make two while loops to skip duplicate 
numbers for left and right so we don't use the same numbers again. Finally, we return the result.
'''

# Optimal Solution was obtained without watching video on 3/4/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums) - 2):

            if a > 0 and nums[a] == nums[a - 1]:
                continue  
            l = a + 1
            r = len(nums) - 1
            while (l < r):
                total = nums[a] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[a],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

# My solution - OPTIMAL on 3/24/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):

            # To find the duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total  = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

# My solution - OPTIMAL on 6/3/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if (total < 0):
                    left += 1
                elif (total > 0):
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while ((left < right) and nums[left] == nums[left - 1]):
                        left += 1
        return res

# My solution - OPTIMAL on 7/20/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
    
            while (left < right):
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while (left < right) and nums[left] == nums[left - 1]:
                        left += 1

        return res

# My solution - OPTIMAL on 7/26/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while(left < right):
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while ((left < right) and nums[left] == nums[left - 1]):
                        left += 1
        return res
