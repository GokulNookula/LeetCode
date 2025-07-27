# OPTIMAL Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hashmap info
        # Key = cols aka column number and set is basically 
        # all values particularly in that column
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        #key = (row/3, col/3) aka 9 total squares
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # To check if we have already had the 
                # same number in that particular row or column or square
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                # // means floor division to round down stuff
                board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                # Adding to that particular column
                cols[c].add(board[r][c])
                # Adding to that particular row
                rows[r].add(board[r][c])
                # Adding to that particular 3x3 sub matrix
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

'''Explained: Time Complexity: O(n^2) Space Complexity: O(n)
'''
