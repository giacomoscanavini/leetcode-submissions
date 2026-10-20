class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        elif len(nums) == 2: 
            return max(nums)
        else:
            robA, robB = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                robA, robB = robB, max(robA + nums[i], robB)

            return robB