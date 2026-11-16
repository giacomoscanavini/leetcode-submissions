class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time complexity: Worst case scenario O(m * n)
        # Space complexity: Modify in-place the grid O(1)
        # m = len(grid), n = len(grid[0])

        # Edge cases
        # Main code
        def dfs(i, j):
            if grid[i][j] == '0': return

            # Remove piece of island from the grid
            grid[i][j] = '0'
            # Search N, S, W, E for other parts of the island to remove
            if i-1 >= 0:    dfs(i-1, j) # N
            if i+1 < nRows: dfs(i+1, j) # S
            if j-1 >= 0:    dfs(i, j-1) # W
            if j+1 < nCols: dfs(i, j+1) # E

        nRows, nCols = len(grid), len(grid[0])
        islandCounter = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == '1': 
                    # If an island is found, increment counter and delete island
                    islandCounter += 1
                    dfs(i, j)

        return islandCounter