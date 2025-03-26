# OPTIMAL Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
'''
Explained: Time Complexity: O(n) Space Complexity: O(1)
To not use regex or any for loop or any builtin function we basically
first make a helper function to convert things into ascii value and check
if it is within that range by using ord(). If it is then we return it
Next in the Palindrome function we make a Two Pointers and basically check if
l and r is the same and if they are a special character then we increment or decrement
that pointer as necessary by calling alphaNum to check it. If it is not the same alphanumeric
then we return false and if it is then we return True. Basically this code is to save on Space Complexity
'''

# My solution not Optimal because of Space

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Implemented a Filter aka Regex to only pass alphabets and numbers
        # Regex Space Complexity is O(n)
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i = 0
        j = len(s) - 1

        while(i < j):
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

'''
Explained: Time Complexity: O(n) Space Complexity: O(n)
First we make a regex function that only lets through alpha numeric values aka
to remove anything that is not. Then we create two pointers called i and j
where we iterate through the entire array and check if i and j are the same
and if they are we continue or else we return False and it is not a palindrome
'''

# My solution not Optiml on 3/25/2025
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def alphaNum(char):
            return (
                (ord(char) >= ord('a') and ord(char) <= ord('z')) or
                (ord(char) >= ord('A') and ord(char) <= ord('Z')) or
                (ord(char) >= ord('0') and ord(char) <= ord('9'))
            )
        
        l = 0
        r = len(s) - 1

        while (l < r):
            if alphaNum(s[l]) == False:
                l += 1
                continue
            if alphaNum(s[r]) == False:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
'''
Almost close to the original optimal solution
'''
