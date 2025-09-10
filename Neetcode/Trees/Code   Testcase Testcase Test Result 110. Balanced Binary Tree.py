# OPTIMAL Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Using a DFS approach using Bottom-Up approach
        def dfs(root):
            # Once we hit the bottom of the tree aka
            # root is a child Node which is None
            if root is None:
                # Then we return if that node's tree
                # is valid and the height of that tree
                return [True, 0]
            
            # Doing the DFS approach going to the left most
            # part of the tree until we hit None
            left = dfs(root.left)
            # Doing the DFS approach going to the right most
            # part of the tree until we hit None
            right = dfs(root.right)
            
            # Checking if our left side of tree is balanced from before
            # so we dont have to do the repetition process and same for right
            # and then get the absolute height between left and right is less
            # than equals to 1 per the question
            balanced = (left[0] == True and
                        right[0] == True and 
                        abs(left[1] - right[1]) <= 1)

            # Finally we return if the tree is balanced from the root
            return [balanced, 1 + max(left[1], right[1])]
        
        # Getting only the boolean as we dont have to do the repeition
        # thus saving time
        return dfs(root)[0]

'''Explained: Time Complexity: o(n) and Space Complexity: O(h) where h is the height of tree
'''
