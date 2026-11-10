class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Fixed number of variables O(1)
        # n is len(nums)
        maxSum = nums[0]
        currentSum = nums[0]

        # This is Standard Kadane for max subarray
        for n in nums[1:]:
            currentSum = max(currentSum + n, n)     # First compare current value with currentSum + current value, reset currentSum if current value is bigger
            maxSum = max(maxSum, currentSum)        # Then update the max

        return maxSum