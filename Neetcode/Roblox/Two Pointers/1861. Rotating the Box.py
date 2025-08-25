# OPTIMAL Solution
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Obtaining the total rows and columns of the box
        rows, cols = len(boxGrid), len(boxGrid[0])

        # We first iterate through all the rows of
        # the unflipped matrix and move all the stones
        for r in range(rows):
            # We start i which keeps track of
            # the empty box where the stone should move to
            # which starts from right to left
            i = cols - 1
            # We start our column array also from the right to left
            # this is due to the gravity problem
            for c in reversed(range(cols)):
                # Checking if the boxgrid is a stone in our
                # column box we are iterating over
                if boxGrid[r][c] == "#":
                    # Swapping the values from the column grid box where the stone is
                    # to the i'th pointer which points to the empty box
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    # Moving our i'th pointer as we occuipied that space
                    # so we go down
                    i -= 1
                # Checking if the boxgrid is a obstactle in our
                # column box grid we are iterating over
                elif boxGrid[r][c] == "*":
                    # Then we need to move our i'th pointer to
                    # column - 1 as column box is a obstacle so
                    # we do not want i'th to be set to it
                    i = c - 1
        
        # To keep our rotated clockwise matrix using
        # INPLACE METHOD
        res = []
        
        # Go through each column as we are rotating it
        for c in range(cols):
            # Storing our new row after rotation
            # from the old column that we get to be
            # pushed into our result array aka our matrix
            cols = []
            # Iterating from the last row of the array
            # from bottom to top
            for r in reversed(range(rows)):
                # Appending each of the boxes into our
                # new row array
                cols.append(boxGrid[r][c])
            # Once getting all the boxes from the old column matrix
            # which is our new rows for our flipped matrix we
            # append all of the column array into it
            res.append(cols)
        return res

'''Explained: Time Complexity: O(m *n) and Space Complexity: O(m * n)
