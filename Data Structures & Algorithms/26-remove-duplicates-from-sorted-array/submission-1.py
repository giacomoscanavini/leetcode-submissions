class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums + Rereferencing O(n)
        # Space complexity: Modify in-place of array O(1) 
        # n is len(nums)

        # There is pointer that scans all numbers and compares to the previous one
        # There is a point that identifies the next one to update
        i = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]: 
                # If they are the same move to the next one
                continue
            else:
                # If they are different, then copy it to the one pointed by i
                nums[i] = nums[j]
                # Update i to the next one available
                i += 1

        return i