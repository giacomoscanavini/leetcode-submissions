class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums + Rereferencing O(n)
        # Space complexity: Modify in-place O(1)
        previous = ''
        k = 0
        r = len(nums) - 1
        current_count = 0
        while r >= 0:
            if nums[r] == previous:
                if current_count < 2: 
                    current_count += 1
                    k += 1
                else: 
                    nums.pop(r)
            else:
                previous = nums[r]
                current_count = 1
                k += 1

            r -= 1
        
        return k