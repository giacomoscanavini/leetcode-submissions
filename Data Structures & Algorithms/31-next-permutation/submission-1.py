class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find pivot (nums[i] < nums[i+1])
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]: 
                pivot = i
                break
        # Swap pivot values with first bigger value from right traverse
        if pivot == -1: 
            nums.reverse()
            return

        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        # Reverse the rest of the array after pivot
        nums[pivot + 1 :] = reversed(nums[pivot + 1:])