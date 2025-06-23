# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initalizing where we set the previous to a nullptr
        prev = None
        # Our current pointer is our head
        curr = head

        # Iterate until our current pointer is a nullptr
        while curr:
            # Store the current next pointer index where it is pointing to
            nxt = curr.next
            # Setting current next pointer to our previous pointer
            curr.next = prev
            # Updating previous pointer to our current pointer
            # to continue our program
            prev = curr
            # Next we need to bring our next pointer array that we stored before
            # and set it to current pointer so we can continue reversing it
            curr = nxt
        # Returning the reversed list
        return prev

'''Explained Time Complexity: O(n) and Space Complexity: O(1)
'''

# My solution - OPTIMAL on 6/22/2025
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
