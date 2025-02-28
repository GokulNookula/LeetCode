# OPTIMAL Solution

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We do not need to fill in 0's because the stack is initalized already
        result = [0] * len(temperatures)
        # Arrange the stack as pair: [temperature, it's index]
        stack = []

        for i, temperature in enumerate(temperatures):
            # Checking if our stack is empty or if it isn't
            # Let us check if our temperature is greater than
            # the top of the stack and the bottom of the stack
            while stack and temperature > stack[-1][0]:
                # If the above condition is true then we pop
                # Both the stack temperature and index
                stackTemp, stackIndex = stack.pop()
                # To compute the index to find the greater
                # temperature for that number of days
                result[stackIndex] = (i - stackIndex)
            # We append the current temperature we are working on
            # to the stack
            stack.append([temperature,i])
        return result

'''Explained: Time Complexity: O(n) Space Complexity: O(n)
So we basically to solve this problem we use a Monotonic Decreasing Stack
where basically the top is the smallest number. To solve the problem we have a stack
where we arrange it as a pair of [temperature, index from the orginial list]. Next we 
make another array filled with 0s of the same size of the temperatures to hold the results.
Now we make a for loop where we keep track of the index and the temperature by using enumerate.
Now we go into the while loop to check if our stack is empty or not and if it is not then we check
if our currentTemp is greater than our top and bottom of our stack and if it is then we pop that pair
out of our stack. Next we compute the number of days aka result by doing current index - popped index
then after all of it we append the current number and index into the stack as a array pair[,]. Then
after the for loop we return the result.
'''
