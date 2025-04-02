# OPTIMAL Solution - beacause it is isn't O(26 * n) instead it is O(n)
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
