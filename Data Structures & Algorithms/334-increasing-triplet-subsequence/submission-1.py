class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3: return False

        one, two = float('inf'), float('inf')
        for num in nums:
            if num <= one: 
                one = num
            elif num <= two:
                two = num
            else: 
                return True

        return False