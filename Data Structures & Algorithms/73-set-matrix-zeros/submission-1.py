class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time complexity: Loop over the matrix O(m * n)
        # Space complexity: Create two sets up to O(m + n)
        # n is number of cols, m is number of rows
        rows_to_zero = set()
        cols_to_zero = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows_to_zero: matrix[r][c] = 0
                if c in cols_to_zero: matrix[r][c] = 0