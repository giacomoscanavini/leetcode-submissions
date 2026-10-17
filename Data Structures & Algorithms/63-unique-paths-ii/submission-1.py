class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1: return 0

        row_above = [0] * ncols
        row_above[0] = 1

        for j in range(1, ncols):
            if obstacleGrid[0][j] == 0:
                row_above[j] = row_above[j - 1]

        for i in range(1, nrows):
            row = [0] * ncols

            if obstacleGrid[i][0] == 0:
                row[0] = row_above[0]

            for j in range(1, ncols):
                if obstacleGrid[i][j] == 0:
                    row[j] = row[j - 1] + row_above[j]

            row_above = row

        return row_above[-1]