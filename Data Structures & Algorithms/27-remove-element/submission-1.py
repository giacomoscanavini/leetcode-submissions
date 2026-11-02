class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Time complexity: Loop over nums + rereference addresses after pop in the middle O(n)
        # Space complexity: Modify in place O(1)
        k = 0
        r = len(nums) - 1 
        while r >= 0:
            if nums[r] == val:
                nums.pop(r)
            else:
                k += 1

            r -= 1
        
        return k