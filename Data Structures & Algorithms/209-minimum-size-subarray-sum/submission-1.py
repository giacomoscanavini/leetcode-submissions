class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Fixed number of variables O(1)
        minLength = float('inf')
        l = 0
        currentWindow = 0
        for r in range(len(nums)):
            currentWindow += nums[r]
            
            while currentWindow >= target:
                minLength = min(minLength, r - l + 1)
                currentWindow -= nums[l]
                l += 1

        if minLength == float('inf'): return 0
        else: return minLength 