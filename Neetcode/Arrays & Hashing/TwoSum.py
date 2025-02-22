# OPTIMAL Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mydict:
                return [mydict[complement], i]
            mydict[nums[i]] = i
'''
Explained: Time complexity: O(n) Space Complexity: O(n)

We have a for loop where we add the numbers into an unorderd hashmap
where we take the complement aka result of target - the current number
then later we check if the complement exists in the hashmap and if it does
we return the index of it along with the index of the current number
and if not we add the current number aka key along with its index aka i 
'''
