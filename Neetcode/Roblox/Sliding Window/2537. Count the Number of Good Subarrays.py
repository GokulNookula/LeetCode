# OPTIMAL Solution
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # To keep track of number of times that
        # number appears in our window
        freq = defaultdict(int)
        # Initalizing our sliding window
        left = 0
        # Total number of pairs we have in our window
        pairCount = 0
        # To store total number of good sub arrays we found
        # aka result
        goodSubArr = 0

        # We are going with an expanded window
        # until our pairCount exceeds k
        for right in range(len(nums)):
            # Incrementing the pairCount by the total
            # number of frequency of that number we found
            pairCount += freq[nums[right]]
            # Since we added a new number to our window
            # we must find it in our freq dictonary and
            # increment it
            freq[nums[right]] += 1

            # When we notice that our size of our pairCount
            # is greater than our total k pairs we 
            # move our left pointer
            while pairCount >= k:
                # We find the total goodArrays aslong
                # as we have pairCount > k
                # We find this by the total length
                # of our array minus the window aka right
                # pointer and add it to our goodSubArr
                goodSubArr += len(nums) - right
                # We need to decrement our value
                # we removed aka the left pointer
                freq[nums[left]] -= 1
                # Decrementing the pairCount also
                # as we removed a value
                pairCount -= freq[nums[left]]
                # Incremeting to continue this loop
                # until we hit false
                left += 1
        # Total number of good sub arrays found
        return goodSubArr

'''Explained: Time Complexity: O(1) and Space Complexity: O(n)
'''
