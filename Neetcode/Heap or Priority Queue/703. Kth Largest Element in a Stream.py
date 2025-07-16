# OPTIMAL Solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # To heapify a list of numbers we call this to get a min heap
        heapq.heapify(nums)
        # Initalizing the object minHeap object that stores all
        # of them based on the top is going to be the smallest number
        self.minHeap = nums
        # This is the total restricted size of the heap and it should
        # not exceed this size
        self.k = k        

    def add(self, val: int) -> int:
        # To add an element into a minHeap
        heapq.heappush(self.minHeap, val)
        
        # We basically loop to check after we add a new element
        # if we passed the size of the minHeap then we pop
        # until the size of the minHeap is less than or equal
        # to size of k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Returning the smallest value after balancing the size
        # of the minHeap
        return self.minHeap[0]    

'''Explained: Time Complexity: O(m * log k) where m is the number of calls made to add() and k is the size of nums Space Complexity: O(k)
'''
