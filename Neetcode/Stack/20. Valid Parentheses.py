# OPTIMAL Solution

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch not in closing:
                stack.append(ch)
            else:
                if stack and stack[-1] == closing[ch]:
                    stack.pop()
                else:
                    return False

        return not stack

'''Explained: Time Complexity: O(n) Space Complexity: O(n)

'''


# My Solution - OPTIMAL too  on 4/1/2025

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")" and (len(stack) != 0 and stack[-1] == "("):
                stack.pop()
            elif s[i] == "}" and (len(stack) != 0 and stack[-1] == "{"):
                stack.pop()
            elif s[i] == "]" and (len(stack) != 0 and stack[-1] == "["):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
''' Time Complexity: O(n) Space Complexity: O(n) '''
