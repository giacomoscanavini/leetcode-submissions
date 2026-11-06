class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Time complexity: Loop over rows and cols O(n^2)
        # Space complexity: Create 3 lists of sets with worst case O(n^2)
        # n is number of rows
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxs = [set() for x in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if value != '.':
                    b = 3 * (r//3) + c//3

                    if value in rows[r]: return False
                    else: rows[r].add(value)

                    if value in cols[c]: return False
                    else: cols[c].add(value)

                    if value in boxs[b]: return False
                    else: boxs[b].add(value)

        return True