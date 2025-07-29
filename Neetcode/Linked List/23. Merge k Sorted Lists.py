# OPTIMAL Solution
        # Edge cases where if there lists contains 1 empty list or the
        # length of lists is 0 then we return nothing
        if not lists or len(lists) == 0:
            return None
        
        # Iterating where we take pairs of linked lists and
        # merging them each time until we have only 1 linked list 
        # remaning aka our output
        while len(lists) > 1:
            # Appending the new merged lists into an array to store
            # the output
            mergedList = []
            
            # Iterating over each of the lists as we put 2 for 
            # iterator because we are merging two pairs at a time
            for i in range(0, len(lists),2):
                # List 1 the first list we merge
                l1 = lists[i]
                # List 2 the second list we merge but we need
                # to make sure it is not an odd number we are merging
                # thus we check it by (i + 1) aka that list is in bound
                # by less than length of the lists and if it is ODD then
                # it is okay to merge a NULL lists with an actually lists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merging the two lists with using a helper function
                # and also appending it into our stored mergedList array
                # in order to keep track of all the merged lists
                mergedList.append(self.mergeList(l1,l2))
            # Updating our lists variable where we were getting our lists
            # from
            lists = mergedList
        # Returning the 1 remaining list aka the merged list
        return lists[0]

    def mergeList(self,l1,l2):
        # Initalizing the new list with a dummy pointer
        dummy = ListNode()
        tail = dummy

        # Iterating the loop until one of these lists is a null pointer
        # as if it is then we deal with it later at the end
        while l1 and l2:
            # Checking if list 1 value is less than list 2 value
            if l1.val < l2.val:
                # Inserting the lower value list to the end of our new list
                # to store the sorted values
                tail.next = l1
                # Updating our list 1 to next pointer of it
                l1 = l1.next
            else:
                # Inserting the lower value list to the end of our new list
                # to store the sorted values
                tail.next = l2
                # Updating our list 1 to next pointer of it
                l2 = l2.next
            # Updating tail pointer so we do not overwrite our 
            # new node we appended
            tail = tail.next
        
        # If list 1 still has values and list 2 does not
        if l1:
            # Then we append all of its values into the end of the new
            # sorted list
            tail.next = l1
        # If list 2 still has values and list 1 does not
        if l2:
            # Then we append all of its values into the end of the new
            # sorted list
            tail.next = l2

        # Returning the sorted two lists merged into one list
        # aka merge part of the algorithm
        return dummy.next


''' Explained: Time Complexity: O(n log k) where k is total number of lists and n is total number of nodes in k list Space Complexity: O(k)
In this algorithm we use merge sort algorithm to solve this problem where we first deal with the edge cases where if the lists has 1 empty
list or the length of lists is empty then we just return None. Next we have a while loop where we iterate until our lists only contains 1 
lists aka our output. Next we initalize a variable called mergeList to store all the merged outputs from over the entire period. Next
we have a for loop that goes from 0 to len(lists) aka total length of lists but our step iteration is moving by 2 because we are merging
two paris at a time. Next we initalize l1 which is easy aka the current list where i is pointing to but for l2 it is tricky as we have edge
case where if our len(lists) is currently odd then we just return None as we can still merge a NULL list with an valid list. Next we append
our merged lists from our helper function where we send l1 and l2.

Helper function: Here we initalize a new linked list to store all the sorted nodes in ascending order. To do it we must check if l1 and l2
lists are not pointing to null then we iterate or else we end the while loop. Next in the while loop we check if l1 value is less than l2
value then we append the l1 value as a new node into the new linked list we created and append it to the tail of it and then we update l1
to point to the next and we do the same for l2 if l2 is less than l1 value. Then if one of the lists is empty and the other still has values
we do the check where if l1 is not pointing to NULl then we append the entire list from that point to the tail of the new linked list and vice
versa for the l2 list if l1 is NULL and finally we return the dummy.next aka the head of the new linked list we created which is the merged
version of them

Finally back to the main function we update our lists to our mergedList aka the array we created to store all the mergedLists which were
broken before and are finally merged together to one big list then we return it by calling lists[0] aka the head
'''

# My solution - OPTIMAL on 7/13/2025
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
''' Explained: Time Complexity: O(n log k) where k is total number of lists and n is total number of nodes in k list Space Complexity: O(k)
'''

# My solution - Almost solved it on 7/29/2025
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists and len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0,len(lists),2):

                l1 = lists[i]

                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeLists(l1,l2))

            lists = mergedList
        return lists[0]

        
    def mergeLists(self,l1,l2):
        dummyNode = ListNode(0)
        tail = dummyNode

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1 != None:
            tail.next = l1
        elif l2 != None:
            tail.next = l2
        return dummyNode.next
