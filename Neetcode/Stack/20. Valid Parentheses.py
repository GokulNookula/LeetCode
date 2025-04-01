# OPTIMAL Solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

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
