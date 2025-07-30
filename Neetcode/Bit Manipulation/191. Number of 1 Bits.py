# OPTIMAL Solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        # To store the number of 1's we found
        count = 0

        # Iterating through the entire bit number
        while n:
            # Basically we first subtract 1 aka the
            # right most bit from the n aka the number
            # and then we AND those two numbers together
            # thus basically getting rid of any 1's where it
            # is a zero in our n - 1 number. Then we increment
            # the count by 1 as we did it by 1 operation and
            # everytime we subtract 1 from the n aka the number
            # the other bits shift right to fulfill it and the
            # AND operator takes care of if there is extra 1's
            # that should not be there
            n = (n & (n - 1))
            count += 1
        # Finally returning the count value
        return count        
'''Explained: Time Complexity: O(1) Since there is only 32 bits and Space Complexity: O(1)
'''
