# OPTIMAL Solution
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # Mapping charCount to list of Anagrams

        for s in strs:
            # Making a list of a ... z for every string
            count = [0] * 26

            for c in s:
                # Converting it to ASCII and increasing it's count
                # for everytime we find that exact character
                count[ord(c) - ord("a")] += 1

            # Appending to matching words together or making a new list if not
            res[tuple(count)].append(s)

        return list(res.values())

'''
Explained: Time Complexity O(m * n) Space Compleixty O(n*m)  m = Length of the Input Array
Here we first make a Hashmap aka Dictonary of lists to store grouped anagrams
Then we iterate through the input list aka strs and in there we make a table of 26 aka 
a ... z and we store that into a hashmap and 
In the next for loop we iterate in each word the character and convert it to ascii and
we increment it based on the character we found.
Then finally we check if that pattern of count of words already exists in the current Hashmap
and if it does we combineit together as a list and if not we create a new list and append it
Finally we output the list of resulted values aka the words keys are the count from a...z

example:
defaultdict(
<
class
'list'
>
, {(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'],etc
'''

# Slower way but easier to write
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

'''
Explained: Time complexity: O(n*m log m) Space Complexity: O(n*m) m = Length of the input array
Here we also make a default dictonary and in the for loop we go through each word
Then we sort each word on a..z where a is first and z is last and arrange them.
Then we map them the words that have the same characters together and append them into a hashmap aka
dictonary and if not we make a new one.
Then we finally return the list of values aka where they key is the sorted word aka like eat = aet
and we find words which have the same instances and group them and if they dont have one we create a new one

example:
defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
'''

# My solution - OPTMAL on 3/24/2025
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myHash = {}
        def asciiVal(s):
            # Instead of just summing ASCII, count how many times each char appears
            # Create a 26-length tuple for 'a' to 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)
        
        for s in strs:
            key = asciiVal(s)
            if key not in myHash:
                myHash[key] = [s]
            else:
                myHash[key].append(s)
        return list(myHash.values())

# My solution - OPTIMAL on 7/26/2025
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[]]
        
        myHash = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            myHash[tuple(count)].append(s)

        return list(myHash.values()) 
