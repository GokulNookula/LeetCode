# OPTIMAL Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Using DFS Base case where we reach the next node of
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

  '''Explained: Time Complexity: O(n) and Space Complexity: O(n) due to recursive stack
  '''
