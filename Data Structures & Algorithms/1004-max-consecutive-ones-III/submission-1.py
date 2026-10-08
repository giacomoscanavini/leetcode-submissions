class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxZeros, maxOnes = 0, 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                maxZeros += 1

            while maxZeros > k:
                if nums[i] == 0: 
                    maxZeros -= 1
                i += 1

            currOnes = j - i + 1
            if currOnes > maxOnes: 
                maxOnes = currOnes

        return maxOnes