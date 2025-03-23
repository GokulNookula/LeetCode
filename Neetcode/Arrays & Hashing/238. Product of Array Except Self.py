# OPTIMAL Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Creating a size of num array with 1 as placeholders
        resultArr = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            # To store the prefix number first to avoid having weird
            # behaviours for the first index HERE WE SET IT
            resultArr[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(len(nums))):
            # To store the value first so we do not have weird behaviours
            # from the last index HERE WE MULTIPLY IT
            resultArr[i] *= postfix
            postfix *= nums[i]
        return resultArr

  '''Explained: Time Complexity: O(n) Space Complexity: O(1)
  So first we make a output array with the same size of nums array filled with 1. Next
  we need to add prefix of all the numbers from nums into output array. So to set the beginning
  we basically set our prefix array beginning as 1 then we start our for loop by storing our current
  prefix number because we store any number that has occured before it. Next we need to multiply our current
  number with the prefix number for the next iteration. Thus we continue doing this loop. Next in order to start our
  postfix array. We first have to start postfix where we iterate from the nums array in reverse. We must set postfix
  starting number as 1 so we do not change the number in the postfix end number. Next we start the for loop in reversed and instead of
  just putting the number in our output array. We must multiply that number with the prefix calculated number and then we
  have to update our update our postfix number stored by multiplying it with our current index of nums that we are iterating. Thus
  next we finally can return the result. The reason why our space complexity is O(1) is because the output array does not count as
  space used thus it is O(1).
'''

# My solution - Not Optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)

        prefix[0] = 1
        suffix[len(nums) - 1] = 1

        for i in range(1,len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2,-1,-1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res
