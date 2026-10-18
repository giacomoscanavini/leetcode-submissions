class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: 
            return n

        stepA, stepB = 1, 2

        for i in range(3, n+1):
            stepA, stepB = stepB, stepB + stepA

        return stepB