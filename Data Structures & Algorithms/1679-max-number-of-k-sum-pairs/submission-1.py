class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nOps = 0
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1
        while i < j: 
            if nums[i] + nums[j] == k: 
                nOps += 1
                i += 1
                j -= 1
            else:
                if nums[i] + nums[j] > k: 
                    j -= 1
                else:
                    i += 1

        return nOps
        