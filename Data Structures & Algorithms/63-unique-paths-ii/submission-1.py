class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Time complexity: Loop over all cells of grid O(m * n)
        # Space complexity: Changes happen in-place O(1)
        # m is len(obstacleGrid), n is len(obstacleGrid[0])
        if obstacleGrid[0][0] == 0: obstacleGrid[0][0] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    # Not an obstacle
                    if j > 0 and obstacleGrid[i][j-1] < 0:
                        # Paths from left
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
                    if i > 0 and obstacleGrid[i-1][j] < 0:
                        # Paths from above
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]

        if obstacleGrid[-1][-1] < 0: return -obstacleGrid[-1][-1]
        else: return 0