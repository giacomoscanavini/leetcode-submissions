class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums, Loop over nums O(n^2)
        # Space complexity: Create array of states O(n)
        # n is len(nums)
        
        # Create array of states
        dp = [1] * len(nums)

        for i in range(len(nums)):
            # Consider all values in the array
            for j in range(i):
                # If any value before nums[i] is less, then update array of state
                # Update with max between itself or state j + 1
                # Keep looping up to the value before i
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The longest is the max in the array of states
        return max(dp)