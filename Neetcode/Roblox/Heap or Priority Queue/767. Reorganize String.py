from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Our Hashmap that stores how many instances of
        # each character we have seen in the string
        count = Counter(s)
        maxHeap = []

        # Adding each character into a maxHeap to be able to
        # obtain the most frequent element in linear time
        for char, cnt in count.items():
            # Count is negative to make it a maxHeap
            heapq.heappush(maxHeap, [-cnt, char])

        # To store the previous character we used so we dont
        # reuse the same character
        prev = None
        # The result string we will return
        res = ""

        # Iterating until maxHeap length is 0 or prev is None
        while len(maxHeap) != 0 or prev != None:
            
            # If our previous has an element but our maxHeap
            # is empty then we have already appened prev value
            # before thus we will have two same characters together
            # thus we need to return None
            if prev != None and len(maxHeap) == 0:
                return ""

            # Getting the most frequent character from
            # the maxHeap
            cnt, char = heapq.heappop(maxHeap)
            # Appending it to the end of the result string
            res += char
            # Increasing the count as we are keep cnt as
            # negative number we reuse until it is 0
            cnt += 1

            # Checking if our prev value was already holding
            # an element then
            if prev != None:
                # To prevent overwriting our prev array and
                # losing it we need to appending it back to our
                # maxHeap
                heapq.heappush(maxHeap, prev)
                # Setting it to None to clear our previous character
                # before we assign a new value to it
                prev = None

            # Checking if the character we just added to result
            # is not 0 then we set our previous result to keep
            # track of the duplicates
            if cnt != 0:
                prev = [cnt, char]

        # Returning our result of final string which does not
        # have same values besides each other
        return res

'''Explained: Time Complexity: O(n) and Space Complexity: O(1) for hashtable and O(n) for output string aka res
'''
