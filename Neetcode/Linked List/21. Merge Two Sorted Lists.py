# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initalizing a new node list with a dummy head as nullpointer
        dummy = ListNode(-1)
        # Adding a tail to append any new nodes to the end of the list
        tail = dummy

        # While both lists are not pointing to a nullpointer we iterate
        while list1 and list2:
            # If our list1 node is less than list2 node
            if list1.val < list2.val:
                # We append the list1 node to the new list we created at the tail of it
                tail.next = list1
                # We update our list1 by going to it's next node
                list1 = list1.next
            # If our list2 node is less than or equal to list1 node
            else:
                # We append the list2 node to the new list we created at the tail of it
                tail.next = list2
                # We update our list2 by going to it's next node
                list2 = list2.next
            # Updating our tail to go to the next node aka keep pointing it at dummy node
            tail = tail.next
        
        # We attach either one of the lists that are not fully iterated to the tail.next node
        # of our new linked list created
        tail.next = list1 if list1 else list2
        # Returning dummy.next because dummy head is a pointing to nullpointer for
        # preventing weird errors
        return dummy.next

'''Explained: Time Complexity: O(n+m) and Space Complexity: O(1)
'''

# My solution - OPTIMAL on 7/29/2025
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
