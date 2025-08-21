# OPTIMAL Solution
class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {")": "(", "}": "{","]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] not in mydict:
                stack.append(s[i])
            else:
                if stack and mydict[s[i]] == stack[-1]:
                    del stack[-1]
                else:
                    return False
        return len(stack) == 0
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''
