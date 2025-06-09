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
In this question we know that we need to keep track of the order of parentheses. This should give us an idea that
we need to use a stack which keeps track of data as LIFO. Thus next we need to create a dictonary where we keep track
of the closing brackets and the key value set to the opening bracket for removing it. This should make our program 0(1)
to validate it. Now we need to iterate throughout the entire string by checking each character. If our current character
is not a closing bracket then we append it into the stack. If is a closing bracket then we first check if our stack is not
empty by doing if stack and then we check if the top of the stack is similar to the opening bracket which is obtained by the dictonary when
our character is a closing bracket and if this case matches. Then we remove the top of the stack by popping the opening bracket out.
Or if our stack is empty and we are still left with closing brackets then we return False as we know that there is no need to keep iterating
as we need a opening bracket before a closing bracket. Then finally we do a return of not stack aka which checks if the stack is empty then
it will return True. Thus this is a O(n) iteration as we are only going through the array only once. It is O(n) in Space Complexity as 
we do not know how long the string is going to be.
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

# My solution - OPTIMAL on 6/8/2025
class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] not in closing:
                stack.append(s[i])
            else:
                if stack and closing[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0) 
