# OPTIMAL Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case where we reach the end of the tree
        # doing bottom up approach checking both child nodes
        # are empty
        if p is None and q is None:
            return True
        # We continue the tree if p node is not a child node and q node
        # is not a child node and p node value is the same as q node value
        if p != None and q != None and p.val == q.val:
            # We call the function itself by moving to the left most part of the tree
            # and coming back up and doing the right most part if it exists
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # Since p or q node is empty and the other one is not empty hence
        # it is not the same tree so we return False
        else:
            return False
'''Explained: Time Complexity: O(n) and Space Complexity: O(h) where h is height of the tree
'''
