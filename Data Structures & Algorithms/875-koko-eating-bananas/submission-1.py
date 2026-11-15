class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Time complexity: Loop over piles + Binary search O(n)
        # Space complexity: Create array for sum O(n)
        # n = len(piles)

        # Edge cases

        # Main code
        l, r = 1, max(piles)+1
        while l < r:
            m = (l + r)//2
            time = sum([x//m if x%m == 0 else x//m + 1 for x in piles])
            if time > h: 
                l = m + 1
            else: 
                r = m 

        return l