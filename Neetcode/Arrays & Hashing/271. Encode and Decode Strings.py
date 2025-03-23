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
            length = int(s[i:j])
            # First character after the delimitar aka 4#e and e is the starting point
            res.append(s[j + 1: j + 1 + length])
            # Reading the next word
            i = j + 1 + length
        return res

  '''Explained: Time Complexity: O() Space Complexity: O()
  '''
