# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initalizing a dummy node so we can keep track of
        # previous element while reversing elements
        dummy = ListNode(0, head)
        # Initalizing a previous pointer
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr != None and k > 0:
            curr = curr.next
            k -= 1
        return curr
'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''

# My solution had the idea couldn't solve it though - OPTIMAL on 7/13/2025
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        left = head
        right = head

        while True:
            numK = k
            right = left
            while numK > 0 and right != None:
                right = right.next
                numK -= 1
            if numK > 0:
                break
        
            prevNext = prev.next
            curr = left
            prevSub = right

            while curr != right:
                temp = curr.next
                curr.next = prevSub
                prevSub = curr
                curr = temp
            
            prev.next = prevSub

            prev = prevNext
            left = right

        return dummy.next
