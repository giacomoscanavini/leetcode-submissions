class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # Time complexity: O(n*S) with memoization, O(2^n) worst case
        # Space complexity: O(n*S) with memoization, O(2^n) worst case
        # n is len(nums), S is sum(abs(x) for x in nums)

        dp = {}
        n = len(nums)
        def recursive(i, total):
            if i == n: 
                # Check condition to end recursive process
                if total == target: 
                    # The sequence of operations reached the target
                    return 1 
                else:
                    # The sequence of operations didn't reached the target 
                    return 0
            else:
                # Continue the recursive process
                if (i, total) in dp.keys(): 
                    # Include caching to speed up the process if a path has already been evaluated
                    return dp[(i, total)]
                else:
                    # Store in dictionary a given node results by summing results from adding and subtracting next value
                    dp[(i, total)] = recursive(i+1, total+nums[i]) + recursive(i+1, total-nums[i])
                    return dp[(i, total)]

        return recursive(0, 0)