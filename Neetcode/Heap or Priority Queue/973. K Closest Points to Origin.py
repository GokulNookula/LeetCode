# OPTIMAL Solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initalizing a minHeap to store the smallest distance values
        # along with the points
        minHeap = []
        # Iterating over each point in the points array
        for x, y in points:
            # Calculating Euclidean distance since x2, y2 is always
            # (0,0) hence the equation becomes this
            dist = (x ** 2) + (y ** 2)
            # We append the distance we found as minHeap will
            # organize it based on that along with keeping track
            # of x and y for that distance
            minHeap.append([dist, x, y])
        # We convert the array to a minHeap here as the above
        # we just appended it into an array so now it will be
        # organized to be able to always get the smallest value
        # that will be on top
        heapq.heapify(minHeap)
        # Array to store our results of k pops from minHeap
        res = []
        # Running it until we get k number of min solutions in
        # our result array
        while k > 0:
            # Extracting the data from our minHeap and organizing it
            dist, x, y = heapq.heappop(minHeap)
            # Appending only the x,y aka our result of min distance values
            # based on what we want for output
            res.append([x, y])
            # Lowering it every iteration
            k -= 1
        # Outputting the result array of k number of min points    
        return res
'''Explained: Time Complexity: O(k log n) where n is the total points length and k is number of points returned Space Complexity: O(n)
'''

# My solution - OPTIMAL on 7/16/2025

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((x**2) + (y**2))
            heapq.heappush(minHeap, (distance,x,y))
        
        for i in range(k):
            distance,x,y = heapq.heappop(minHeap)
            res.append([x,y])

        return res
