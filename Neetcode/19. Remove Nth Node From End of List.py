# OPTIMAL Solution
        # Initalizing the dummy node giving it a value of 0 and saying it's 
        # next node is head or we just do dummyNode.next = head
        dummyNode = ListNode(0, head)
        # Initalizing two points
        left = dummyNode
        right = head

        # Initalizing right pointer to be n distance from left pointer
        while n > 0 and right != None:
            right = right.next
            n -= 1
        
        # Looping until the right pointer reaches to the end of the list
        # we are stopping the loop when we are basically at where left pointer
        # next node is the n value and right pointer is at the end
        while right != None:
            # Doing this in the beginning to deal with the dummynode initalization
            left = left.next
            right = right.next

        # We break as the right pointer reached the end of the list
        # Now we basically need to delete the value we dont want which
        # was setup above
        left.next = left.next.next

        # Returning our answer
        return dummyNode.next

'''Explained: Time Complexity: O(n) and Space Complexity: O(1)
'''
