# OPTMAL Solution

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l = 0
        r = len(height) - 1
        res = 0

        # Initalizing the maxleft and right pointers
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            # We update the maxLeft pointer only when it is smaller than the maxRight
            # This is so we can store water
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                # This will never be negative as we are updating maxLeft first
                # before we even add the total number of droplets
                res += maxLeft - height[l]
            # We update the maxRight pointer only when it is smaller than the maxLeft
            # This is so we can store water     
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                # This will never be negative as we are updating maxRight first
                # before we even add the total number of droplets
                res += maxRight - height[r]
        return res

'''Explained: Time Complexity: O(n) Space Complexity: O(1)
This solution is better than using the prefix and postfix method as we do not store anything in arrays. So 
first we make sure to pass the testcase where if the height array is empty then we return 0 since we do not need to
iterate. Next we setup the left pointer to the beginning of the array and right to the end of the array. We also initalize
the maxleft pointer and maxright pointer as this will help us keep track of how much water we can store near that height area.
Now we start our while loop and make sure that the left pointer is less than right pointer. Next we need to only move the either of
the max pointer if it is less than the other aka if our maxLeft pointer is less than the maxRight pointer or we move our maxRight pointer
if it is less than maxLeft pointer. We also need to take into another edge case where if both pointers are equal you can move either one. Here
I choose to move the maxLeft pointer. Next inside the if statement after updating the left pointer since it was less by increasing the left pointer by 1. 
We must also make sure to update our maxLeft based on if it is greater than our current left pointer we are iterating. Next we need to check if there was
any water collected which is done by adding it to result by doing maxleft - current height of left pointer. Since we update the maxLeft before thus we
never have to deal with a negative value being added into result. Next in our else statment we decrement right pointer by 1 if maxRight is less than 
maxLeft. We also update our maxRight pointer to check if our current height of right pointer is greater than our maxRight. We also make sure to check
if we caught any water by adding it to the result based on maxRight - current height of right pointer. Same case since we update maxRight before we never
deal with negative values. Then once all of it is done we return our result. Thus this process helps us prevents increasing space complexity. Thus optimal
'''
