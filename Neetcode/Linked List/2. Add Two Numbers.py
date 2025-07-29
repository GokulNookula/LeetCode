# OPTIMAL Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a new list to store all the added number
        # of the nodes we create
        dummy = ListNode()
        cur = dummy
        # Initalizing a variables that can store the carry over excess
        # since our values in the node have to be between 0-9
        carry = 0
        # Iterating the loop until list1 or list2 is at nullpointer or
        # until our carry number is 0 aka None
        while l1 or l2 or carry:
            # We update v1 value if l1 element exists else we set it to 0
            v1 = l1.val if l1 else 0
            # We update v2 value if l2 element exists else we set it to 0
            v2 = l2.val if l2 else 0

            # Adding up all the values to find our new value for the
            # newNode we create
            val = v1 + v2 + carry
            # Storing how much we need to carry over for the next number
            carry = val // 10
            # To obtain only the number between 0-9 for the newNode
            val = val % 10
            # Appending the newNode to the end of the new list 
            # that keeps track of added two numbers
            cur.next = ListNode(val)

            # Updating our current pointer so we can append 
            # the next two sum newNode created
            cur = cur.next
            # Checking if we reached the end of list1 then we
            # set it to None so we end the while if the other one is false
            l1 = l1.next if l1 else None
            # Checking if we reached the end of list2 then we
            # set it to None so we end the while if the other one is false
            l2 = l2.next if l2 else None

        # Returning the head of the new list of added two numbers
        return dummy.next

''' Explained: Time Complexity: O(m+n) where m = len(l1) and n = len(l2) Space Complexity: O(max(m,n)) aka max length of one of the list that is longer
In this problem first we initalize to create a new list that stores our summed up nodes that we need to 
return. Next we create a variable that stores the carry over number since our summed newNode can only 
store numbers between 0-9 thus we need to carry over that number to the next node for iteration. Now 
we create a while loop where we iterate until list1 and list2 points to null pointer and carry number
is equal to 0 or else wecontinue iterating throughout the list. Now we initalize two variables like v1 
and v2 which stores the value of the pointer at l1 and l2 so we can use it for addition for finding the 
summed up number or else we set them to 0 since l1 or l2 is pointing to a null pointer thus we set their 
value to 0. Next we sum up v1, v2 and carry to obtain our new value we get. Next we need to find if it is 
greater than 9 then we obtain the carry number by  floor dividing it by 10 to obtain the carry over number. 
Next we get the new value number between 0-9 by doing modulus division by 10. Next we append the newNode we 
create to the new list that stores all the sum of two number newNodes to the next of the current pointer. 
Next we update our current pointer to not overwrite our newNode we just added. Next we need to check if our 
l1 and l2 is currently pointing to a null pointer aka at the end of the list then we return None so we can 
end our while loop else we update them to point to the next pointer. Then finally once we are done with the while loop we
return the head of the new list of sum of two nodes we created.
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

# My solution - OPTIMAL on 7/13/2025
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # We update v1 value if l1 element exists else we set it to 0
            if l1 != None:
                v1 = l1.val
            else:
                v1 = 0
            if l2 != None:
                v2 = l2.val
            else:
                v2 = 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

            if l1 != None:
                l1 = l1.next
            else:
                l1 = None
            if l2 != None:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next

# My solution - OPTIMAL on 7/29/2025
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        curr = dummyNode
        carry = 0

        while l1 or l2 or carry:
            if l1 != None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
            else:
                val2 = 0
            
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

            if l1 != None:
                l1 = l1.next
            else:
                l1 = None
            if l2 != None:
                l2 = l2.next
            else:
                l2 = None
        return dummyNode.next
