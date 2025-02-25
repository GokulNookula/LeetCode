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

We basically make 
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
