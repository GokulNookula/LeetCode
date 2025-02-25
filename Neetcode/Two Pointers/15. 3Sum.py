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

We basically first make an array to store all the results and also sort all the numbers in the array in
ascending order. Then we make a for loop and set 1 of the values. Then we check if k is above 0 and check if
we already have that element 
