class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Time complexity: Loop over the numbers O(n)
        # Space complexity: Fixed number of variables O(1)
        l, r = 0, len(numbers)-1
        while l < r: 
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                return [l+1, r+1]