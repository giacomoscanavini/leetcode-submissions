class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxZeros, maxOnes = 0, 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                maxZeros += 1

            while maxZeros > 1: 
                if nums[i] == 0:
                    maxZeros -= 1
                i += 1
                
            maxOnes = max(maxOnes, j - i)
        
        return maxOnes
