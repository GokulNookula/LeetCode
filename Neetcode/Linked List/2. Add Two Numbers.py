# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

'''Explained: Time Complexity
'''
# My solution - does not work on 7/1/2025

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(0, None)
        sumNode = dummyNode
        carryOver = 0
        addingVal = 0
        curr1 = l1
        curr2 = l2

        while curr1 != None and curr2 != None:
            addingVal = curr1.val + curr2.val + carryOver
            if addingVal >= 10 and curr1.next != None and curr2.next != None:
                addingVal = addingVal - 10
                carryOver = 10
                newNode = ListNode(addingVal, None)
                sumNode.next = newNode
                sumNode = sumNode.next
            elif addingVal >= 10 and curr1.next == None and curr2.next == None:
                newNode = ListNode
            else:
                newNode = ListNode(addingVal, None)
                sumNode.next = newNode
                sumNode = sumNode.next
            curr1 = curr1.next
            curr2 = curr2.next
        return dummyNode.next

