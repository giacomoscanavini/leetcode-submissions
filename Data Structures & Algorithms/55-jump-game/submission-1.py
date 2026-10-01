class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1: return True
        else:
            if nums[0] == 0: return False

            steps = 0
            for num in nums:
                if steps < 0: return False
                elif num > steps: steps = num
                steps -= 1

            return True

        