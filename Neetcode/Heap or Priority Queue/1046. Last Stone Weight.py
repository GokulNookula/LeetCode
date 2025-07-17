# OPTIMAL Solution

'''Explained: Time Complexity: O() Space Complexity: O(k)
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
