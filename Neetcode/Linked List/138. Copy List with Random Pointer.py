# OPTIMAL Solution
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Creating a hashmap to store the deep copy nodes first where
        # we map every old node to the copy of that node we created
        oldToCopy = {None: None} # 

        # Initalizing our beginning of our pointer to keep track to not
        # loose the head
        curr = head

        # First pass where we are cloning the linked list nodes
        # and adding it into the hashmap and nothing is being connected
        while curr != None:
            # Creating a copy of the old node
            copy = Node(curr.val)
            # Mapping the old node to the copy we just created
            oldToCopy[curr] = copy
            # Updating current pointer so we can iterate over it
            curr = curr.next
        
        # Resetting our current pointer to beginning of the old nodes
        curr = head
        # Second pass where we link all the copy nodes aka now we set
        # the pointers of the linked list
        while curr != None:
            # To obtain back our copy node that was created in the first pass
            copy = oldToCopy[curr]
            # Setting the next pointer of copy by calling it from the hashmap
            # since we can obtain the old next node and just use hashmap to find
            # the copy address
            copy.next = oldToCopy[curr.next]
            # Setting the random pointer of copy by calling it from the hashmap
            # since we can obtain the old next node and just use hashmap to find
            # the copy address for the random pointer too
            copy.random = oldToCopy[curr.random]
            # Updating current pointer so we can iterate over it
            curr = curr.next
        # Returning the head of the copy list
        return oldToCopy[head]

  '''Explained: Time Complexity: O(n) and Space Complexity: O(n)
  '''

# My solution - Almost solved it on 7/29/2025
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldCopy = {None:None}

        curr = head

        while curr != None:
            copy = Node(curr.val)
            oldCopy[curr] = copy
            curr = curr.next
        
        curr  = head

        while curr != None:
            copy = oldCopy[curr]
            copy.next = oldCopy[curr.next]
            copy.random = oldCopy[curr.random]
            curr = curr.next

        return oldCopy[head]
