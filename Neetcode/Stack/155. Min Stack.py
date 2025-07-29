# OPTIMAL Solution

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

'''
Explained: Time Complexity: O(1) Space Complexity: O(n)
We know that a regular stack the time complexity for push, pop and top is O(1). But to
make getMin O(1). We have a seperate stack that tracks the minimum number at each level of the
original stack. Basically we have two stacks. But the minStack's main goal is to track the minimum
value at that level. So when appending a value we first append the value to regular stack then
we check if the current value is smaller than the current top of our minstack and also make sure
that it is not empty and hold the result and then append that result into the minstack. For pop we
pop both stacks at the same time. For getting the top of a stack we do it for regular stack. For getMin
we just return whatever is on the top of the minStack. Thus making it easier.
'''

# My Solution - Almost Optimal 4/1/2025
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) != 0 and (val < self.minStack[-1]):
            self.minStack.append(val)
        elif len(self.minStack) != 0 and (val > self.minStack[-1]):
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
    def pop(self) -> None:
        del self.stack[-1]
        del self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

# My solution - OPTIMAL on 7/26/2025
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack and val < self.minStack[-1]:
            self.minStack.append(val)
        elif len(self.minStack) != 0:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        del self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
