# OPTIMAL Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

'''
Explained: Time Complexity: O(n) Space Complexity: O(1)
We basically first check if both the arrays are the same length to consider it
as an anagram. Then we create a count array of length 26 thus limiting the space and
we only use 1 array instead of using two hashmaps. Then we increment count everytime
we found a character in the string s and we decrement the count of the character of
everytime we find it in the string t. Then we have another for loop to check if all the
values in the count array is 0 and if it is then it is an anagram else it is False. Thus
by limiting the space we reduce the space complexity of the problem making it optimal.
'''


# My Solution is not Optimal
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hashMapS:
                hashMapS[s[i]] += 1
            elif s[i] not in hashMapS:
                hashMapS[s[i]] = 1
            if t[i] in hashMapT:
                hashMapT[t[i]] += 1
            elif t[i] not in hashMapT:
                hashMapT[t[i]] = 1
        if hashMapS == hashMapT:
            return True
        else:
            return False
'''
Explained: Time Complexity: O(n) Space Complexity: O(n) (because it was not limited to 26 characters)

We create two hashmaps aka one for each string and make a for loop where we add the character into the
hashmap if it is not already in that certain string hashmap and set the value to 1. If it already does 
exist then we increase the count by 1. Then finally we check if both of the hashmaps are the same if it is
then we return True or else we return False. This algorithm can be made faster by using ASCII values and
limiting the keys to 26 characters only.
'''
