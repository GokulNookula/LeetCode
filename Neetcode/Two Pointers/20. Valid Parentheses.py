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
'''
Explained: Time Complexity: O(n) and Space Complexity: O(n)
This solution is faster because we use less if else statements to check stuff
so basically we create a dictonary and then append if the current character is not a
closing bracket and if it is a closing one then we check if the stack is empty first and
then we check if the top of the stack has the opening bracket by using the dictonary and if it
is then we pop and finally we check if the stack is empty or not and return True if it is empty.
Main reason it is better is because we use less checking statements aka if-else thus making it faster
'''

# My solution

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
                stack.append(s[i])
        return (len(stack) == 0)
'''
Explained: Time Complexity: O(n) and Space Complexity: O(n)
We create a list aka a stack where we push parentheses if they
are open and if they are a closing parentheses then first we check
if our stack is empty or not and then we check if the top of our stack
contains that or not and if it does we pop or else we append it to the stack
Then finally we check if the stack is empty then we return True or else
we return False
'''
