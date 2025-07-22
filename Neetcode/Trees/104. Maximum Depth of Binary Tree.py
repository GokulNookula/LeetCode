# OPTIMAL Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Doing Recursive DFS where
        # we initalize base case when we hit the childern
        # we return 0 for depth
        if root is None:
            return 0

        # First going to the left most node and traverse backup
        # once we hit the child
        left = self.maxDepth(root.left)
        # Next going to the right most node and traverse backup
        # once we hit the child
        right = self.maxDepth(root.right)

        # Returning the maxDepth between left and right tree
        # adding + 1 as we are moving up the tree as we
        # need to recurse back up
        return max(left, right) + 1
      
'''Explained: Time Complexity: O(n) (where best case is O(log n) and worst case
is O(n)) Space Complexity: O(n)
'''

# My solution - Didn't Solve it on 7/21/2025
# Using Iterative DFS 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        stack = [(root, 1)]
        while len(stack) != 0:
            node, depth = stack.pop()

            if node != None:
                maxDepth = max(depth, maxDepth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return maxDepth
