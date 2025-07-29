# OPTIMAL Solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking Solution
        # only add open paranthesis if open < n
        # only add a closing parathensis if close < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backTrack(openN, closeN):
            # Base case
            if openN == closeN == n:
                # We take every character in the stack and join them
                # into an empty string to form a complete string that
                # is eventually appended into our result array
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                # Recursively continue our backtrack by incrementing
                # the count for open as we appended it
                backTrack(openN + 1, closeN)
                # We need to update the stack by popping the character
                stack.pop()
            if closeN < openN:
                stack.append(")")
                # Recursively continue our backtrack by incrementing
                # the count for open as we appended it
                backTrack(openN, closeN + 1)
                # We need to update the stack by popping the character
                stack.pop()
        # For our inital function calling
        backTrack(0,0)
        return res

'''Explained: Time Complexity: O(O(4 N/Sqrt(N)) Space Complexity: O(n)
We basically use backtracking where we use a stack to append our current combination of
parentheses and once we are completed with the combination we append it into the result.
Fisrt we make a base case where we check if the number of open parentheses and closed parentheses
are equal to n. If so then we start appending the result into the stack by making an empty string first
and joining it so we result our answer as a string. Next we need to make a case where we check if number of
open parentheses is less than n and if so we append one into the stack and we call backtrack and increment the
count of open parentheses and we also make sure we pop the character out from the stack after adding it. Next
we need to make another case to check if our closed parentheses count is less than open parentheses as we cannot
have closed parentheses count aka appended before the open and if so we append it into the stack and increment
the count and call backTrack and we also make sure to pop it out of the stack. Now finally we need to also make the
base case of starting the backTrack algorithm. And finally we return our result.
'''

# My solution - Didnt solve it on 7/26/2025
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")

                backTrack(openN + 1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")

                backTrack(openN,closeN + 1)
                stack.pop()
        backTrack(0,0)
        return res 
