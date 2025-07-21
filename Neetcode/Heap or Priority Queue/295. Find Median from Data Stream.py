# OPTIMAL Solution
class MedianFinder:

    def __init__(self):
        # Both these heap sizes must be equal
        # in order to solve this problem
        self.minHeapForLargeVal = []
        self.maxHeapForSmallVal = []

    def addNum(self, num: int) -> None:
        # Pushing every value we get into the maxHeap to store
        # the smallest numbers in order to get the middle as
        # a negative value since there is no maxHeap in python
        heapq.heappush(self.maxHeapForSmallVal, -1 * num)

        # Checking if the both heaps are not empty and
        # Making sure that every number in maxHeapForSmallVal is less than
        # or equal to every number in minHeapForLargeVal FOR VALUE DIFFERENCE
        if (self.maxHeapForSmallVal and self.minHeapForLargeVal
            and (-1 * self.maxHeapForSmallVal[0] > self.minHeapForLargeVal[0])):
            # Since maxHeap root is greater than minHeap value
            # we need to reorder it so we pop the maxHeap value
            val = -1 * heapq.heappop(self.maxHeapForSmallVal)
            # We push the new value into our minHeap to make sure
            # to satisfy our order
            heapq.heappush(self.minHeapForLargeVal, val)

        # Checking if the length difference between two heaps is
        # greater than 1 then we reorder the heaps adding 1 to deal with
        # 0 also being counted FOR SIZE DIFFERENCE
        if len(self.maxHeapForSmallVal) > len(self.minHeapForLargeVal) + 1:
            # We pop the value from the maxHeap and push it to the minHeap
            # to balance the trees
            val = -1 * heapq.heappop(self.maxHeapForSmallVal)
            heapq.heappush(self.minHeapForLargeVal, val)
        # Checking if the length difference between two heaps is
        # greater than 1 then we reorder the heaps adding 1 to deal with
        # 0 also being counted the other way around
        if len(self.minHeapForLargeVal) > len(self.maxHeapForSmallVal) + 1:
            # We pop the value from the minHeap and push it to the maxHeap
            # to balance the trees
            val = heapq.heappop(self.minHeapForLargeVal)
            heapq.heappush(self.maxHeapForSmallVal, -1 * val)

    def findMedian(self) -> float:
        # Checking if the length between two heaps are odd then
        if len(self.maxHeapForSmallVal) > len(self.minHeapForLargeVal):
            # Return the top value of maxHeap aka the small value
            return -1 * self.maxHeapForSmallVal[0]
        # Checking if the length between two heaps are odd the other
        # way around then
        if len(self.minHeapForLargeVal) > len(self.maxHeapForSmallVal):
            # Return the top value of minHeap aka the large value
            return self.minHeapForLargeVal[0]
        
        # When the heaps are even then we sum both the roots of heap
        # and divide by 2 to get the median
        return ((-1 * self.maxHeapForSmallVal[0] + self.minHeapForLargeVal[0]) / 2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

'''Explained: Time Complexity: O(m∗logn) for addNum(), O(m) for findMedian() (where m is number of
calls and n is the length of the array) Space Complexity: O(n)
'''
