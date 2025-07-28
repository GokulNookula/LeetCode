# OPTIMAL Solution

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Testcase when if t is empty string
        if t == "":
            return ""

        # Setting up the hashmaps for countT and current window
        countT = {}
        window = {}

        # Initalizing the countT hashmap as it does not change
        for c in t:
            # Basically finding the value in hashmap if found increase it by 1
            # or else we default the value to 0 by .get and increment it by 1 aka
            # set it to 1
            countT[c] = 1 + countT.get(c, 0)
        # This is for storing how many matches we found from s and t
        have = 0
        # The total characters in the string t that we must match for s
        need = len(countT)
        # Storing the left and right pointer of the substring we found
        res = [-1, -1]
        # Storing the smallest substring length and updating if we dont find it
        resLen = float("infinity")
        l = 0
        # Iterating through every character in s
        for r in range(len(s)):
            # Getting aka storing the current character we just reached
            c = s[r]
            # Basically finding the value in hashmap if found increase it by 1
            # or else we default the value to 0 by .get and increment it by 1 aka
            # set it to 1
            window[c] = 1 + window.get(c, 0)

            # Check if we satisfied the count window for the first time or not
            # and we check if c character is in countT
            if ((c in countT) and (window[c] == countT[c])):
                # Increment the have as we met the condition
                have += 1
            # We try reduce the window size if we met the condition
            while have == need:
                # Checking if our window is smaller than the previous one
                if (r - l + 1) < resLen:
                    # Updating our result
                    res = [l, r]
                    resLen = (r - l + 1)
                # We need to pop from left until we dont meet the have == need
                # Thus to find the smallest substring of t in s
                window[s[l]] -= 1
                # Checking if decrementing it caused the have to go down
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # If it did then we reduce it
                    have -= 1
                l += 1
        # Extracting the left and right pointer from the result array to check stuff
        # in the return function
        l, r = res
        # We do s[l: r + 1] + 1 for off by 1 adjustment and we do this to check
        # if resLen has been updated aka case where if a result does not exist 
        # then we return an empty string or else we return s[l: r + 1]
        return s[l : r + 1] if resLen != float("infinity") else ""

'''Explained: Time Complexity: O(n) Space Complexity: O(m)
'''

# My solution - Didnt solve it on 7/28/2025
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        countT = {}
        window = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if ((c in countT) and (window[c] == countT[c])):
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                window[s[left]] -= 1
                if ((s[left] in countT) and window[s[left]] < countT[s[left]]):
                    have -= 1
                left += 1
            
        left, right = res

        return s[left : right + 1] if resLen != float("infinity") else ""
