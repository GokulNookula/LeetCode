# OPTIMAL Solution
class Solution:

    def encode(self, strs: List[str]) -> str:
        # This is the result that we are returning is an entire sentence
        res = ""
        for s in strs:
            #Adding our formula of length of string + delimitar + actual string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # We are returning as list of strings
        res = []
        i = 0

        while i < len(s):
            # Second pointer
            j = i
            while s[j] != "#":
                j += 1
            # s[i:j] = s[0:1] = "5" how it looks
            length = int(s[i:j])
            # First character after the delimitar aka 4#e and e is the starting point
            res.append(s[j + 1: j + 1 + length])
            # Reading the next word
            i = j + 1 + length
        return res

'''Explained: Time Complexity: O(m) Space Complexity: O(m+n)
To encode and decode the list of strings. First, to encode the list of string we must
create an empty string that holds the entire encoded string then we iterate through each
string in the list of string and we append it into the empty string in a way where we first
append the length of the string we are reading and then we add a delimiter to show where does the
string end and then we finally add the string. Thus with this process we are able to read a string
and keep track of the length of the string in the encoded message even when the string has our delimiter
or any special characters inside it. Next we have to decode the string that we encoded back into a list of
string. So first we must make a two pointers and in there in our first while loop we must end it if we reach
the end of the encoded string and in our second pointer we set it the same as i. Next we start our next while loop
where we check if the current string the second pointer is reading is a delimiter or not. If it is not a delimiter then
we increase the counter of j or else we get out of the for loop and we have to next retrive our length of the next string which
is currently in the format of a string which needs to be converted into an integer. Next since we still haven't appended into our
result list we must do it here where we start appending anything after j + 1 which is anything after the delimiter and till the end
of the length of the string which we reterived before. Next we must update i to read the next word by setting it's value after the end
of the string aka j + 1 + length. Thus we have solved the encoding and decoding problem.
'''

# My solution - could not solve 3/24/2025
class Solution:
    def encode(self, strs: List[str]) -> str:
        encodeString = ""

        for s in strs:
            encodeString += str(len(s)) + "#" + s
        
        return encodeString

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

# My solution - Almost solved it on 7/26/2025
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedS = ''

        for s in strs:
            encodedS += str(len(s)) + "#" + s
        
        return encodedS

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
