class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        # Time complexity: Get a slice of n elements O(n)
        # Space complexity: Create a slice of n elements O(n)
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]