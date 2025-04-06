# OPTIMAL Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # To ignore any duplicates from added into the different substrings
        charSet = set()
        # First pointer in Sliding Window beginning
        left = 0
        # To store our longest substring number
        res = 0

        # Second pointer in the sliding window
        for right in range(len(s)):
            # If our substring has a duplicate character in substring
            # We iterate until we remove it
            while s[right] in charSet:
                # Removing the duplicate character from the left aka beginning
                charSet.remove(s[left])
                # Updating the count of our left index beginning for new substring
                left += 1
            # If it is not a duplicate then we increase the length of substring
            charSet.add(s[right])
            # Updating every iteration to check if our current substring is bigger
            # than our previous maximum substring length. 1 is added to fix the
            # length as we start left from 0
            res = max(res, right - left + 1)
        return res
      
'''Explained Time Complexity: O(n) n = length of string Space Complexity: O(m) m = The total number of unique characters in the string
In this problem the difference between a substring and a subsequence is that substrings do not contain any duplicate characters. Thus this
hint should give us that we need to store our result in a set to remove any duplicates. Next in order to iterate throughout the string to find the
longest substring we must add it to our current substring and check if we added any duplicate characters. So in order to keep a track of this we
use the method of sliding window aka two pointers. Here we set the left pointer to the beginning of the main string aka beginning point of substring.
Next we also need to initalize a variable to store the longest substring length. Next we make our right pointer dynamically update based on the length of
the input string aka iterate only once throughout it aka making this O(n). Next we need to check if our character in the right pointer already exists 
in our set and if it does then we must remove the characters from the left until we remove that character from our left pointer and set that as our new
beginning point for our left pointer. Thus we first remove the left character from our current substring and then we increment our left pointer. If we do not
have a duplicate in our set then we add the current character from the right pointer into the set. Then we also need to check if our current length of our substring
is bigger than our previous maximum result aka longest substring if we do then we update it or else it keeps the result. Then once we iterate fully from the loop
we return our longest substring value. Thus since we are using a set our length of our set is the total number of unique characters in the string making it O(m).
'''

# My solution on 4/5/2025
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength
