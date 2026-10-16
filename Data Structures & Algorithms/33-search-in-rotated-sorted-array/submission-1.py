class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = i + (j - i)//2
            if nums[m] == target: 
                return m
            
            if nums[i] <= nums[m]:
                # Left side is sorted
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            
            else:
                # Right side is sorted
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
            
        return -1