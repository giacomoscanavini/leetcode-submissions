class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Fixed number of variables O(1)
        if len(nums) == 1: return True
        if nums[0] == 0: return False
        
        available_steps = 0
        for n in nums:
            if available_steps < 0: return False
            if n > available_steps: available_steps = n
            available_steps -= 1

        return True