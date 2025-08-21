# OPTIMAL Solution
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # To store all the different types of colours
        # it will store how many of that colour we have
        colors = [0] * n
        # Output storage
        res = []
        # Variable to store the number of adjacent
        # equal pairs we found
        count = 0

        # Going through all the queries
        for index, val in queries:
            # We need to check the neighbours of that colour
            # we check the leftside and the rightside
            left, right = index - 1, index + 1

            # Remove previous contribution
            # We first check if that index had a previous colour
            # stored then we need to fix our total count paris
            if colors[index] != 0:
                # Checking if left of our array index exists aka not a seg fall
                # and our old colour does math with the left side
                if left >= 0 and colors[left] == colors[index]:
                    # then we decerement as our old pair didnt
                    count -= 1
                # Checking if right of our array index exists aka not a seg fall
                # and our old colour does math with the right side
                if right < n and colors[right] == colors[index]:
                    # then we decrement as our old pair didnt
                    count -= 1

            # Update our colour value at that index
            # then we start incrementing after this
            colors[index] = val

            # Add new contribution
            # First we check if our new value is
            # not a no colour aka 0
            if val != 0:
                # Checking if right of our array index exists aka not a seg fall
                # and our new colour does math with the right side
                if left >= 0 and colors[left] == val:
                    # then we increment our count pair
                    count += 1
                # Checking if right of our array index exists aka not a seg fall
                # and our new colour does math with the right side
                if right < n and colors[right] == val:
                    # then we increment our count pair
                    count += 1
            # Appending our new total pair count to our
            # result array at that iteration
            res.append(count)

        return res
'''Explained: Time Complexity: O(n) and Space Complexity: O(n)
'''
