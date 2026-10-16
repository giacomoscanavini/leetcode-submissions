class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        bounds = [-1, -1]
        # Lower bound
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = i + (j - i)//2
            if nums[m] > target:
                j = m - 1
            elif nums[m] < target:
                i = m + 1
            else:
                if m > 0 and nums[m - 1] == target:
                    j = m - 1
                else:
                    bounds[0] = m
                    break

        # Upper bound
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = i + (j - i)//2
            if nums[m] > target:
                j = m - 1
            elif nums[m] < target:
                i = m + 1
            else:
                if m < len(nums)-1 and nums[m + 1] == target:
                    i = m + 1
                else:
                    bounds[1] = m
                    break

        return bounds