# OPTIMAL Solution



''' Explained: Time Complexity: O() Space Complexity: O()
'''

# My solution - Maybe OPTIMAL? on 7/13/2025
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a minHeap to store all the values
        minHeap = []

        # Iterate over all the list of linked list
        for i in range(len(lists)):
            # Initalizing a pointer for the beginning of that linked list 
            curr = lists[i]
            # Append the value until we reach the end of that linked list in the list
            # to the heap
            while curr != None:
                heapq.heappush(minHeap, curr.val)
                curr = curr.next
        # Create a linked list to return the merged list from the heap
        dummy = ListNode()
        mergeNode = dummy

        # Iterate until the heap is empty
        while minHeap:
            # Create a node and append the top value of the minHeap to make a
            # ascending order of merged linked lists
            newNode = ListNode(heapq.heappop(minHeap))
            mergeNode.next = newNode
            mergeNode = mergeNode.next
        # Return the head of the new merged linked list
        return dummy.next
