class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ncols = n
        nrows = m

        row_above = [1] * ncols
        
        for i in range(1, nrows):
            row = [1] * ncols
            for j in range(1, ncols):
                row[j] = row[j - 1] + row_above[j]
            row_above = row
        
        return row_above[-1]

