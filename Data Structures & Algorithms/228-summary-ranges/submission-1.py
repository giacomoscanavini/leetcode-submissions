class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create strings for output O(n) 
        # n is len(nums)
        if len(nums) == 0: return []
        elif len(nums) == 1: return [str(nums[0])]
        else:
            output = []
            start = str(nums[0])
            end = str(nums[0])
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    end = str(nums[i])
                
                elif nums[i] - nums[i-1] > 1:
                    if start == end: output.append(start)
                    else: output.append(start + '->' + end)
                    start = str(nums[i])
                    end = str(nums[i])

            if start == end: output.append(start)
            else: output.append(start + '->' + end)

            return output