class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create set of nums up to O(n)
        # n is len(nums)
        nums = set(nums)
        maxLength = 0
        for n in nums:
            if n-1 in nums: continue
            else:
                l = 1
                start = n + 1
                while start in nums:
                    l += 1
                    start += 1
                maxLength = max(maxLength, l)
        
        return maxLength