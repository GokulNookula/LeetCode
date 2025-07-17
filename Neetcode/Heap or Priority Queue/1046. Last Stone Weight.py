# OPTIMAL Solution
        # Converting this entire list as negative to simulate
        # maxHeap in python using a minHeap
        stones = [-s for s in stones]
        # Converting the entire list as a heap
        heapq.heapify(stones)

        # Looping until our list only has 1 stone left is
        # when we output
        while len(stones) > 1:
            # Getting the two stones numbers to
            # smash them together
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # We have to check if the second stone is greater
            # than first stone aka they are not equal
            if second > first:
                # Then we need to smash aka do first - second
                # as the second one is bigger but since we are
                # doing subtraction we do it this way as we 
                # convert second number to positive as we minus it
                # negative number and then push that number into
                # the heap as we didnt fully destroy it
                heapq.heappush(stones, first - second)

        # This is to deal with if the length of stones
        # is empty then we return 0 which is done later
        # if not it won't show up as it is a maxHeap
        stones.append(0)
        # Returning the absolute value to ignore negative sign
        return abs(stones[0])
'''Explained: Time Complexity: O(n log n) Space Complexity: O(n)
'''

# My solution - OPTIMAL on 7/16/2025
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negStones = [-x for x in stones]
        heapq.heapify(negStones)
        negStones = negStones

        while len(negStones) >= 2:
            val1 = -heapq.heappop(negStones)
            val2 = -heapq.heappop(negStones)

            if val1 != val2:
                total = val1 - val2
                heapq.heappush(negStones,-total)
            else:
                continue
        if len(negStones) == 1:
            return abs(negStones[0])
        else:
            return 0
