class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c].isdigit():
                    value = board[r][c]
                    b = (r // 3) * 3 + c // 3
                    if value in rows[r] or value in cols[c] or value in boxes[b]:
                        return False
                    else:
                        rows[r].add(value)
                        cols[c].add(value)
                        boxes[b].add(value)
                        
        return True