# OPTIMAL Solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        currLine, length = [], 0

        i = 0

        while i < len(words):
            # Case 1 where the current line is complete
            # Adding length and length of the line which includes the space and
            # the length of our current word if it is greater than maxWidth
            if length + len(currLine) + len(words[i]) > maxWidth:
                # Calculating how many extraspaces we need in between each word
                extraSpace = maxWidth - length

                # Calclating number of spacing that go in between each word as we
                # want it to be as evenly as possible
                # Edge case when length of the line is 1 then we do the
                # max(1, line - 1) to deal with it
                spaces = extraSpace // max(1, len(currLine) - 1)
                # This is to deal with odd extraspaces we distribute in a greedy
                # way from left to right per the question
                remainder = extraSpace % max(1, len(currLine) - 1)

                # Adding spaces into the line in between words and we do - 1 to deal with
                # edge case where length of line is 1 then we just skip this loop for when
                # we need to add spaces at the right aka the last instance of sentence
                for j in range(max(1, len(currLine) - 1)):
                    # Adding spaces to the current word by multiplying the
                    # number of spaces for each one
                    currLine[j] += " " * spaces

                    # Checking if our remainder is 0 or not for extra spaces
                    if remainder != 0:
                        # Doing the greedy way of adding extra spaces
                        # leftover from left to right
                        currLine[j] += " "
                        remainder -= 1

                # Adding all the words together by joining them together
                # Dont need to add the space in "" as we calculated it before hand
                res.append("".join(currLine))
                # Resetting line and length
                currLine, length = [], 0
                continue

            # Case 2 where the current line is not complete
            currLine.append(words[i])
            # The length only includes the characters of the words without the space number
            length += len(words[i])
            i += 1

        # Handling the last line aka the word by
        # adding one space between each word while joining it
        # using as a delimitor to prevent trailing space
        lastLine = " ".join(currLine)
        # Calculating extra space left over
        trailSpace = maxWidth - len(lastLine)
        # Adding those trailing spaces to the right of the
        # word to deal with it
        res.append(lastLine + " " * trailSpace)
        return res
'''Explained: Time Complexity: O(N) Space Complexity: O(N)
'''
