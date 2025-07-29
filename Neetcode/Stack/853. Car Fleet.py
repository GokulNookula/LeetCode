# OPTIMAL Solution

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

'''Explained: Time Complexity: O(n log n) Space Complexity: O(n)
Here since we have two arrays we need to sort the array based on the descemnding order
of the position. Here the Zip function helps us to make it a way where the array is sorted
based on descending order of the position. Next we make a stack. Now we need to iterate through
the paris we made. In order to calculate the time of a car we do (target - position / speed)
where we only append it as an integer. Next we need to make sure that the current car we appended
and the previous car we have do not collide. This is done by checking the length of the stack if it is
greater or equal to 2 and if the current car's time is less than previous car's time and if it is not
we pop it as it will collide which would result it becoming a single fleet itself. If it doesn't collide
then we pop it out of the stack. Next to get the number of different fleets that are itself we return the
length of the stack.
'''

# My solution - Didnt solve it on 7/28/2025
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for position, speed in pair:
            stack.append((target - position)/ speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
