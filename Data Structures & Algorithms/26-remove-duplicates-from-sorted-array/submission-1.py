class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums + Rereferencing O(n)
        # Space complexity: Modify in-place of array O(1) 
        previous = ''
        k = 0
        r = len(nums) - 1
        while r >= 0:
            if nums[r] == previous: 
                nums.pop(r)
            else:
                previous = nums[r]
                k += 1
            r -= 1

        return k