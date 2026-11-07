class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Time complexity: Loop over the board O(m * n)
        # Space complexity: Updates in-place O(1)
        # m is number of rows, n is number of cols
        def filter(r, c):
            count = 0
            for i in [r-1, r, r+1]:
                for j in [c-1, c, c+1]:
                    if 0 <= i < len(board) and 0 <= j < len(board[0]):
                        if i == r and j == c: pass
                        else:
                            if 1 <= board[i][j] <= 2: count += 1

            if board[r][c] == 1 and count < 2: return 2
            elif board[r][c] == 1 and count in [2, 3]: return 1
            elif board[r][c] == 1 and count > 3: return 2
            elif board[r][c] == 0 and count == 3: return 3
            else: return board[r][c]

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = filter(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2: board[r][c] = 0
                elif board[r][c] == 3: board[r][c] = 1
                else: continue