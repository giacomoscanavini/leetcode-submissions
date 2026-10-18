class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        rows = {}
        cols = {}

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(nrows):
            if i in rows.keys():
                matrix[i] = [0] * ncols
                continue
            else:
                for j in range(ncols):
                    if j in cols.keys():
                        matrix[i][j] = 0