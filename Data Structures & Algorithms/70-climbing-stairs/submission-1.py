class Solution:
    def climbStairs(self, n: int) -> int:
        # Time complexity: Loop over n steps O(n)
        # Space complexity: Create fixed number of variables O(1)
        # n is length of staircase

        # Edge cases at the beginning of the staircase
        if n == 1: return 1
        if n == 2: return 2
        
        # Starting number of ways to reach 1st and 2nd step
        N1, N2 = 1, 2
        for i in range(3, n+1):
            # Apply recuriveness and store N2 into N1 at each cycle 
            # This is needed for next step
            N1, N2 = N2, N1 + N2

        return N2