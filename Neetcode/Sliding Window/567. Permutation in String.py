# OPTIMAL Solution
        # Similar to anagram check if s1 is greater then it is false
        # because permutation must be smaller than s2
        if len(s1) > len(s2):
            return False

        # Creating a list size of 26 aka from a to z to store the
        # values of matching from the strings
        s1Count = [0] * 26
        s2Count = [0] * 26 

        # Going through s1 string and adding all of them into the hashmap
        # for both s1 and s2 we do s2 to save time so we partially go through
        # until we end the for loop in s1 as that will be our window size
        for i in range(len(s1)):
            # Incrementing the count based on ASCII values
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # To keep track of how similar both arrays are where 26 means both match
        # and anything less than that then it would be false
        matches = 0
        # Since the arrays are size of 26 thus we only iterate to set them up
        # For our inital matches
        for i in range(26):
            # Checking if at that index s1Count is the same as s2Count
            if s1Count[i] == s2Count[i]:
                # if it is same then we increase match count
                matches += 1
        # Initalize left to beginning of the s2 array
        left = 0
        # We start the right pointer where we ended our s1 array aka it's length
        # This shows how we are using the sliding window
        for right in range(len(s1), len(s2)):
            # We must check if our match was already found then
            # we return true or else we keep going
            if matches == 26:
                return True

            # Getting the index of the right pointer
            index = ord(s2[right]) - ord('a')
            # Incrementing the character that we found by 1
            s2Count[index] += 1
            # If we found a match then we increment the match number by 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it did not match then we decrement matches count by 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # We do the same thing for the left pointer here but instead we subtract
            # because we already have that value stored in our array
            index = ord(s2[left]) - ord('a')
            # Obtaining the index value
            s2Count[index] -= 1
            # If we found a match then we increment the match number by 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it did not match then we decrement matches count by 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            # We shift left pointer by 1 as to preserve our window size to be fixed
            left += 1
        # Checking if we found a permutation then we return true or else not
        return matches == 26

'''Explained: Time Complexity: O(n) Space Complexity: O(1) <- because fixed list size of 26
In this problem we first must check if the size of s1 is greater than s2 as if the permutaiton string must always be
smaller than the string that we are checking similar to anagram. Next we need to initalize two arrays of size 26 as
that is our constrains fromt the question. Next we need to fill the s1 array count. This is done by our first for loop
as we need to initalize our window size for sliding window while doing that we also do the same for s2. Next we need
to check how many matches we have between the two count arrays. This is done by another for loop where we increment if
we find both of the values being similar note the for loop only is 26 because of the size of the count arrays. Next we
need to initalize our left pointer to the beginning of the s2 string. Next we need to initalize our right pointer to the 
end of size of s1 as we already added it into our count array in the first for loop while setting up the window size. Now
we check if our matches is 26 then we return True. If it is not then we convert the value at that index for right pointer into
ASCII value and then check if we have a match then we increment match count by 1 or else we decrement the count by 1. Next
we do the same for the left pointer but instead we need to decrement the count value at the s2 index as it is already in our array.
Next we check if we have a match between s1 and s2 count at that index if so then we increment it by 1 or else we decement it by 1. 
Next in order to maintain the window size we increment left count by 1 thus mainting the size of the window. Finally if we are done
iterating through the s2 loop we check if our matches is 26 then we found permutation and return True or else we return False.
'''

# My solution - ALmost solved it on 4/22/2025
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0

        for right in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            left += 1

        return matches == 26
