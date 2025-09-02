# OPTIMAL Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # We use a Pre-Order DFS where we initalize 
        # the base case when we reach the root we stop
        # the recursion
        if not root:
            return None

        # We swap nodes first then go down
        # Storing the left node to swap nodes
        temp = root.left
        # Assigning left node to the right node
        root.left = root.right
        # Assigning right node to the left node temp val
        root.right = temp
        
        # First iteration we swap the left and right node 
        # of the root then we go to the deepest left
        # node and once we hit the child we recursively
        # loop back and swap the left most tree node first
        # then go to the right most tree node and swap those
        # values
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Returning the root value to get the inverted tree
        return root
        
  '''Explained: Time Complexity: O(n) and Space Complexity: O(n) due to recursive stack
  '''

# My solution - Didnt Solve it myself on 7/21/2025
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Using DFS - POST-order Base case where we reach the next node of
        # the child node is none
        if root is None:
            return None

        # We recursively call itself where we go to the deepest
        # left node and then swap the nodes
        leftRes = self.invertTree(root.left)
        # We recursively call itself where we go to the deepest
        # right node and then swap it
        rightRes = self.invertTree(root.right)

        # Once we are at the child node we basically
        # swap the nodes because we have the previous iteration
        # result stored above
        root.left = rightRes
        root.right = leftRes

        # Returning after we reach to back to the top
        # aka the root
        return root

# My solution - OPTIMAL on 9/2/2025
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        lefRes = self.invertTree(root.left)
        rightRes = self.invertTree(root.right)

        root.left = rightRes
        root.right = lefRes

        return root
