class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Fixed number of variables O(1)
        # n is len(nums)
        maxSum = nums[0]
        currentMax = nums[0]
        minSum = nums[0]
        currentMin = nums[0]
        totalSum = nums[0]

        for n in nums[1:]:
            # Standard Kadane for max subarray
            currentMax = max(currentMax + n, n)
            maxSum = max(maxSum, currentMax)

            # Standard Kadane for min subarray
            currentMin = min(currentMin + n, n)
            minSum = min(minSum, currentMin)

            # Total array cumulative sum
            totalSum += n

        if minSum == totalSum:
            # Edge case in which the entire array is negative, then use Kadane for max
            return maxSum
        else:
            # Compare Kadane for max with the total array cumulative sum minus Kadane for min
            return max(maxSum, totalSum - minSum)