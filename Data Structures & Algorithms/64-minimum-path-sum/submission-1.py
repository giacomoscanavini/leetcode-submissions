class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        row_above = grid[0]
        for j in range(1, ncols): row_above[j] += row_above[j - 1]

        for i in range(1, nrows):
            row = grid[i]
            for j in range(ncols):
                if j == 0: 
                    row[j] += row_above[j]
                else:
                    row[j] += min(row_above[j], row[j-1])
            
            row_above = row

        return row_above[-1]