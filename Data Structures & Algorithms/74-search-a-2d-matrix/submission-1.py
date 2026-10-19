class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Binary search to identify the row with complexity O(log m)
        # Binary search within the identified row with complexity O(log n)
        # Final complexity is given by O(log(m) + log(n)) = O(log m * n)
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        lrow, rrow = 0, len(matrix) - 1
        while lrow < rrow: 
            m = lrow + (rrow - lrow)//2
            if matrix[m][-1] < target: 
                lrow = m + 1
            elif matrix[m][-1] > target:
                rrow = m
            else:
                return True

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l)//2
            if matrix[lrow][m] < target:
                l = m + 1
            elif matrix[lrow][m] > target:
                r = m - 1
            else:
                return True

        return False