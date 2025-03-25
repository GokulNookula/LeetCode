# OPTIMAL Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mydict = {}

        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            elif num in mydict:
                return True
        return False
'''Explained: Time Complexity: O(n) Space Complexity: O(n)
We first create a dictonary to keep track of all the values. Next we make a for loop to iterate
throughout the nums array and now we check if the current number we are iterating over does it
exist or not. If it does not exist then we add it into the dictonary and set it's default value as 1.
Else if there is a duplicate then we do not need to increase the count of the num in the mydict as
the question says if it exists then we just return True. If we do not find any then once the for loop
ends we just return False. Thus this is a linear time complexity solution but the trade off here is we
need more space.
'''
