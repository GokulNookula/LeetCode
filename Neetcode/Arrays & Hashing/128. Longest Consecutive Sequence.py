# OPTIMAL Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method to get run time of O(n) time complexity
        # To remove duplicates from the list
        numSet = set(nums)
        longest = 0

        for n in nums:
            # To check if n is the starting point of a sequence
            # aka not to have a number less than it aka left number
            if (n - 1) not in numSet:
                length = 0
                # Here length is used as a number to keep adding to check if
                # the next number exists while n stays the same.
                # Since it is a hashset the lookup is O(1)
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

''' Explained: Time Complexity: O(n) Space Complexity: O(n)
To find the longest sequence. We find the result by the help of a set.
So basically we first pass the nums in as a set to remove any duplicates in our array as
we do not want to increase the length number if we have the same number iterated. Next
we make a for loop and iterate though the entire array of numbers. Now we need to check if
n is the starting point of a sequence so we check if it is already in the numSet if not we
start our algorithm to increase the length if and only if that number exists in the numSet which
is done in our while loop. Here we start the iteration by checking the inital number and increase our
length everytime the number is in the numSet and if it is not we exit the loop and update our longest
sequence by calling the max between our current length and the previous longest sequence. Once we are
done iterating throughout the loop then we return the longest sequence.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      # My method is O(nlogn) but we need O(n) time complexity
       count = 1
          longSeq = 0
          if (len(nums) == 1):
              return 1
          nums.sort()
  
          for i in range(len(nums) - 1):
              # If the number is 1 more than the current number
              if ((nums[i] + 1) == nums[i + 1]):
                  count += 1
              # If more than what we want we reset the counter
              elif (nums[i] == nums[i + 1]):
                  pass
              else:
                  count = 1
              if (longSeq < count):
                  longSeq = count
          return longSeq
