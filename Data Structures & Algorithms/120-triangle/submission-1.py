class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Time complexity: Operate at each node for n-1 levels O((n-1)*n/2)
        # Space complexity: Modify in-place O(1)
        # n is len(triangle)
        for i in range(len(triangle)-1)[::-1]:
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]