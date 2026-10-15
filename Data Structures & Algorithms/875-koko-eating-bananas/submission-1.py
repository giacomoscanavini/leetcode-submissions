class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 1
        j = max(piles)
        while i < j: 
            m = i + (j - i)//2
            hours = sum([x // m if x % m == 0 else x // m + 1 for x in piles])
            if hours <= h: 
                j = m
            else:
                i = m + 1
        
        return i
            