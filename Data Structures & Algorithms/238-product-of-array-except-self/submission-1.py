class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create arrays O(n)
        # n = len(nums)

        n = len(nums)
        left = [1] * n
        right = [1] * n
        # From left to right
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        # From right to left
        for i in range(0, n-1)[::-1]:
            right[i] = right[i+1] * nums[i+1]
        # Product of each element
        for i in range(n):
            left[i] *= right[i]

        return left