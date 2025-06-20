# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initalizing two pointers one is a slow pointer
        # the second is a fast pointer using concept hare and tortoise
        slow = head
        fast = head

        # Checking if our fast pointer that is being shifted by two points
        # if it is not a nullpointer then we iterate the while loop
        while fast != None and fast.next != None:
            # Shifting slow pointer only by 1 pointer
            slow = slow.next
            # Shifiting fast pointer by 2 pointers
            fast = fast.next.next
            # Checking if the two pointers have met then
            # there is a cycle in the loop
            if slow == fast:
                return True
        # If we don't see a cycle we return False
        return False
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''

# My solution - not optimal on 6/19/2025
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        storedVal = []

        while head:
            if head not in storedVal:
                storedVal.append(head)
            else:
                return True
            head = head.next
        return False
