# OPTIMAL Solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Making a Dynamic array of the size of our bit + 1
        # to keep track of the extra also returning this array
        # which keeps track of our result that we return
        dp = [0] * (n + 1)
        # The offset is to keep track of if we reached the
        # very next 2^n aka next bit raised to remove the
        # repeated work done to compute the other bits in that number
        offset = 1

        # Going from 1 to n + 1 to keep it inclusive and not start at 0
        for i in range(1, n + 1):
            # Checking if our offest can be doubled aka
            # if we reached the next Most Siginificant Bit aka MSB
            if offset * 2 == i:
                # Since we reached it we need to update offset
                # so we can prevent repeated work by help of dynmaic
                # programming
                offset = i
            # Computing the number of 1's in that index aka i value
            # by also keeping track of offset just to prevent repeated work
            dp[i] = 1 + dp[i - offset]
        return dp

'''Explained: Time Complexity: O(n) Space Complexity: O(nlogn) because of recursive stacking
'''

# My solution - Brute Force on 7/29/2025 
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            num = i
            count = 0
            while num:
                num = num & num - 1
                count += 1
            res.append(count)
        return res
  ''' This solution is Time Complexity: O(nlogn) and Space Complexity: O(n)
  '''
