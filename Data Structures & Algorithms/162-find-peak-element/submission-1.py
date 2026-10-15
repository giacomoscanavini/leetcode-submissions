class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            m = i + (j-i)//2

            if nums[m] > nums[m+1]:
                j = m
            else:
                i = m + 1
        
        return j
