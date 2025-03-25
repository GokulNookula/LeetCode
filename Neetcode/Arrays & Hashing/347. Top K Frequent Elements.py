# OPTIMAL SOLUTION

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # To make a dictonary numbers with that count
        count = {}
        # Creating array of buckets which are the size of our array + 1
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # To check if the number exists in the dictonary or not
            # If it does exist we add 1 with the current count aka n
            count[n] = 1 + count.get(n,0)
        # n is the count value aka bucket and c is the number 
        # of keys with that count value
        for n, c in count.items():
            # Appending to the correct bucket
            freq[c].append(n)
        
        # To get the K frequent elements
        res = []
        for i in reversed(range(len(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

'''
Explained: Time Complexity: O(n) Space Complexity: O(n)
We basically use bucket sort where the count number is the buckets.
The number of buckets is the max size of the array aka freq in the code.
Then we store a dictionary of keys aka numbers which have the same count.
The first for loop does that where if not in the Hashmap it gives it a value of 1
and also it increases the value aka count by 1 if it already exists.
The second for loop is basically appending the values into the correct buckets
Then the third for loop basically checks from the max count bucket to the minimum one
and adds the K number of Frequency numbers into the result array and returns it if 
len(res) == k.
'''



# My Solution is not Optimal
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = {}

        for i in range(len(nums)):
            if nums[i] not in myHash:
                myHash[nums[i]] = 1
            elif nums[i] in myHash:
                myHash[nums[i]] += 1
        return heapq.nlargest(k,myHash,key=myHash.get)

'''
Explained: Time Complexity O(n log(k)) and Space Complexity O(n)
We are basically taking a huge list of elements and making a for loop and
check if element exists in the HashTable or not and if it doesnt give it
a starting count value and if it exists then we increase the count.
The heap part basically goes through the array and finds the nlargest
values and returns it from the Hash Table.
'''

# My solution did not solve 3/24/2025
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = {}


        for num in nums:
            if num in myHash:
                myHash[num] += 1
            else:
                myHash[num] = 1
        return heapq.nlargest(k,myHash,key=myHash.get)
