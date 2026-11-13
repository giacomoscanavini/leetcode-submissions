class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Time complexity: Loop over all cells of grid O(n * m)
        # Space complexity: Changes happen in-place O(1)
        # n is len(grid), m is len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0: continue
                elif i == 0 and j > 0:
                    # There is no upper row 
                    grid[i][j] += grid[i][j-1]
                elif i > 0 and j == 0: 
                    # There is no left col
                    grid[i][j] += grid[i-1][j]
                else:
                    # Replace (i,j) with min path to (i,j)
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]