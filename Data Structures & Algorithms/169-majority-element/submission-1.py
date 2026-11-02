class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums and hash map O(n)
        # Space complexity: Create hash_map up to O(n)
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        
        for key,val in hash_map.items():
            if val >= len(nums)//2: return key