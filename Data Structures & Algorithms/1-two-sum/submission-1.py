class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create hashmap up to O(n)
        # n is len(nums)
        hashmap = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            else:
                hashmap[num] = i