class Solution:
    def jump(self, nums: list[int]) -> int:
        # Time complexity: Nested loop with worst case scenario given by overlaps O(n^2)
        # Space complexity: Fixed number of variables O(1)
        if len(nums) == 1: return 0

        jumps = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if start + nums[start] >= end:
                return jumps + 1
            
            next_start = start + 1
            for i in range(next_start, next_start + nums[start]):
                if i + nums[i] > next_start + nums[next_start]:
                    next_start = i

            start = next_start
            jumps += 1

        return jumps