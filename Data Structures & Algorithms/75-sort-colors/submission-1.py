class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort_around_pivot(nums, l, r):
            pivot = nums[r]
            i = l - 1
            for j in range(l, r):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[r] = nums[r], nums[i + 1]
            return i + 1

        def quicksort(nums, l, r):
            if l < r: 
                m = sort_around_pivot(nums, l, r)
                quicksort(nums, l, m-1)
                quicksort(nums, m+1, r)
        
        quicksort(nums, 0, len(nums)-1)