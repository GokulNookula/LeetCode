# OPTIMAL Solution - beacause it is isn't O(26 * n) instead it is O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hashmap to access each character count from string fast
        count = {}
        # The longest repeating character answer stored
        res = 0
        
        # Beginning of the left pointer index
        l = 0
        # To keep track of the longest character sequence 
        maxf = 0
        # Second pointer increases it's size as we iterate over the
        # entire length of the string to track the longest charcter sequence
        for r in range(len(s)):
            # To initalize the character in the dictonary whether if it exists
            # then we just find the current count from dictonary and increase it
            # by 1 or else we initalize it with count.get to 0 and increase it by 1
            count[s[r]] = 1 + count.get(s[r], 0)
            # To keep track of the longest character count to save time in checking
            # for the while loop when removing characters if we exceed k replacement
            maxf = max(maxf, count[s[r]])

            # While windowlength aka (r - l + 1) minus the maximum character in
            # our dictonary of count to get the number of characters count that
            # are not the same character as our maximum character and then we
            # check the number of those characters is less than allowed replacable
            # count given to us aka (windowlen - maxCharacterFreq) > k
            while (r - l + 1) - maxf > k:
                # We decrement the count of that variable from the left as
                # we move our left pointer by 1 to remove it from our dictonary
                count[s[l]] -= 1
                # Moving the left pointer by 1 until we meet the above condition
                l += 1
            # Returning the maximum character length with the replacable characters
            # being replaced already
            res = max(res, r - l + 1)

        # Returning the maximum character
        return res

'''Explained: Time Complexity: O(n) Spac Complexity: O(n)
In this we are going to have a dictionary named count to store all our 26 variables which is not restricted. We also
have a variable that 
'''


# My solution - Almost had it passed 20 cases on 4/1/2025
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        tempK = k
        length = 1
        maxSubstring = 0
        for right in range(1, len(s)):

            if s[left] == s[right]:
                length += 1
            elif k > 0:
                k -= 1
                # Treat as if we replaced s[right] to match s[left]
                length += 1
            elif k == 0 and (len(s) - right) > k:
                left = right
                k = tempK
                length = 1
            else:
                break
            maxSubstring = max(maxSubstring, length)
        return maxSubstring

# My solution (did not solve it) on 4/6/2025
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
