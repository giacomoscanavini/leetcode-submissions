class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        best_guess = 0
        while left <= right:
            m = left + (right - left)//2
            if m * m < x: 
                best_guess = m
                left = m + 1
            elif m * m > x: 
                right = m - 1
            else:
                return m
            
        return best_guess
        