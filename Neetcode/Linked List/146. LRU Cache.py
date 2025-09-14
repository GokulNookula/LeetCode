# OPTIMAL Solution
class Node:
    # Creating a doubley linked list class to be used
    # for the following problem
    def __init__(self,key,val):
        self.key = key
        self.val = val
        # We need to know previous and next for
        # each node that is created
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # It is the max size that our cache can be and
        # it must not exceed and if it does we need to remove
        # the least recently used cache aka number
        self.cap = capacity
        # Dictonary to store all our cache values aka a hashtable
        # that stores a double linked list that is connected
        # where it maps key to a node
        self.cache = {} 

        # Left Dummy node that tells us the least recent value used
        self.left = Node(0,0)
        # Right Dummy node that tells us the most recent value used
        self.right = Node(0,0)

        # Initalizing where these nodes are connected to each other
        # in order to be able to put in a new node in between left
        # and right node
        # Left = LRU node, right = most recent used node
        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove the node from our list
    def remove(self,node):
        # Storing the node previous pointer so we can update
        # it to point to node.next
        prev = node.prev
        # Storing the node next pointer so we can update it
        # to point from node previous to node.next
        nxt = node.next

        # Updating these values as mentioned above
        # without any memory leaks
        prev.next = nxt
        nxt.prev = prev

    # Insert node at right since it is recently
    # been added aka visited by the LRU cache
    def insert(self,node):
        # Getting our right node previous pointer
        # which will point to our new node aka
        # that is added in the middle
        prev = self.right.prev
        # Getting our right node pointer next that is
        # pointed by previous pointer to the right pointer
        # as right pointer is a dummy node hence we send it
        # by itself
        nxt = self.right

        # Setting the two indices to point to the new node
        # that is being added in the middle of previous and right
        # pointer
        prev.next = nxt.prev = node
        
        # Updating our new node pointers to point properly
        # so we do not have memory leaks after setting the previous and
        # right pointer POINTERS pointing to the new node and now
        # we only make the new node point properly to right pointer and
        # previous pointer
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        # Checking if that key exists in our hashmap which
        # is O(1) as per our requirements
        if key in self.cache:
            # Deleting that node from the left most of our list
            # as we are utilizing the node
            self.remove(self.cache[key])
            # After removing the node we need to insert it back on
            # the right most part of our list as it has been recently 
            # used
            self.insert(self.cache[key])
            # Returning the value found for that key since it exists
            # in our hashmap
            return self.cache[key].val
        # Returning -1 since it does not exists in our hashmap
        return -1

    def put(self, key: int, value: int) -> None:
        # Before we insert the new value we need to check if that
        # key and value already exists in our hashmap
        if key in self.cache:
            # If it does exist then we remove it from our hashmap
            self.remove(self.cache[key])
        # Then we create a new node with the same key and value
        self.cache[key] = Node(key, value)
        # Then we insert the node at the right since it was recently
        # added thus recently used
        self.insert(self.cache[key])

        # After we added the value we also want to check if
        # our length of our cache is bigger than our capacity
        if len(self.cache) > self.cap:
            # If it is then we obtain our LRU value since
            # it is in the left most part aka next to the left
            # pointer
            lru = self.left.next
            # We next remove the value from our linked list 
            # so we do not have a memory leak for pointers not
            # pointing properly since removing that node
            self.remove(lru)
            # Finally we delete the LRU value from our hashmap
            # so we can completely wipe it clean from our cache
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

''' Explained: Time Complexity: O(1) for get() and put() Space Complexity: O(n)
'''

# My solution - Almost solved it on 7/29/2025
class Node:
    # Using a doubly linked list aka where
    # we know the previous and next of each node
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

# My solution - Didn't solve it on 9/13/2025

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
