class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        
        n = len(grid)
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1

        counter = 0
        for col in zip(*grid):
            try: 
                counter += rows[tuple(col)]
            except: 
                pass

        return counter