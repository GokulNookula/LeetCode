# OPTIMAL Solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]

'''Explained: Time Complexity: O(n) Space Complexity: O(n)
We basically use a stack where we append if our c is a number into the stack
else if our c is a operator of + or * we pop the stack two times and do the respective
number and then we also append the result back into the stack rather than having a number storing
all the numbers. For operaters like - and / we need to be careful as our total is going to be below
the top. Thus we have to store the numbers as a and b of popped results. Then we have to do b - a for
subtraction and after we append it back. For division we must make sure our number is an integer at the end
so we do int() after that we append it back. Then we finally return the result aka stack[0]
'''

# My solution - Almost similar to optimal code on 4/1/2025
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 1

        for i in range(len(tokens)):
            if tokens[i] == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(b + a)
            elif tokens[i] == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(b - a)
            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                num = int(float(b) / a)
                num = max(num,0)
                stack.append(num)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        
# My solution - OPTIMAL on 7/28/2025
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()

                stack.append(b - a)
            elif tokens[i] == "*":
                stack.append((stack.pop() * stack.pop()))
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()

                stack.append(int(float(b) / a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]      
