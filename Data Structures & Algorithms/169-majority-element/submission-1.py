class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        m = int(n // 2 + n % 2)

        hash_table = {}

        for i in range(n):
            hash_table[nums[i]] = hash_table.get(nums[i], 0) + 1

        for key, value in hash_table.items():
            if value >= m: 
                return key