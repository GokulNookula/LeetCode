# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        # Finding the middle of the list for even or odd one
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        # Reversing the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merging two half of the list
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''

# My solution - Didn't solve it on 7/29/2025
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second != None:
            secondNxt = second.next
            second.next = prev
            prev = second
            second = secondNxt
        
        first = head
        second = prev

        while second != None:
            firstNxt = first.next
            secondNxt = second.next
            first.next = second
            second.next = firstNxt
            first = firstNxt
            second = secondNxt
