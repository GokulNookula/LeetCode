# OPTIMAL Solution
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        res = []
        count = 0

        for index, val in queries:
            left, right = index - 1, index + 1

            # Remove previous contribution
            if colors[index] != 0:
                if left >= 0 and colors[left] == colors[index]:
                    count -= 1
                if right < n and colors[right] == colors[index]:
                    count -= 1

            # Update color
            colors[index] = val

            # Add new contribution
            if val != 0:
                if left >= 0 and colors[left] == val:
                    count += 1
                if right < n and colors[right] == val:
                    count += 1

            res.append(count)

        return res
'''Explained: Time Complexity: O(n) and Space Complexity: O(n)
'''
