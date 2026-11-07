class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time complexity: Loop over half the matrix O(n^2)
        # Space complexity: Change happens in-place O(1)
        # n is number of rows and cols
        nRows = len(matrix)
        nCols = len(matrix[0])
        # Reflection about x-axis
        for r in range(len(matrix)):
            if r == nRows//2: break
            for c in range(len(matrix[0])):
                matrix[r][c], matrix[nRows-1-r][c] = matrix[nRows-1-r][c], matrix[r][c]

        # Transpose
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if c > r: 
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]        