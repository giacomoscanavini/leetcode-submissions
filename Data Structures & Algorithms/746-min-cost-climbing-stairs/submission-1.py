class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        mincostA, mincostB = cost[0], cost[1]

        for i in range(2, len(cost)):
            mincostA, mincostB = mincostB, cost[i] + min(mincostA, mincostB)

        return min(mincostA, mincostB)