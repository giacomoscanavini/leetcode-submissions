class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Time complexity: Loop over all entries in the matrix O(m * n)
        # Space complexity: Create output array O(m * n)
        # n is number of cols, m is number of rows
        nRows = len(matrix)
        nCols = len(matrix[0])
        output = []
        r, c = 0, 0
        
        direction = ['right', 'down', 'left', 'up']
        last_value = [nRows, -1, 0, nCols-1]
        edge = [0, nCols-1]

        d = 0
        while len(output) < nRows * nCols:
            output.append(matrix[r][c])

            if [r, c] == edge: 
                if direction[d] == 'right': 
                    last_value[d] -= 1
                    edge = [last_value[d], edge[1]]
                elif direction[d] == 'down': 
                    last_value[d] += 1
                    edge = [edge[0], last_value[d]]
                elif direction[d] == 'left': 
                    last_value[d] += 1
                    edge = [last_value[d], edge[1]]
                else: 
                    last_value[d] -= 1
                    edge = [edge[0], last_value[d]]
                
                d = (d + 1) % 4

            if direction[d] == 'right': c += 1
            elif direction[d] == 'down': r += 1
            elif direction[d] == 'left': c -= 1
            else: r -= 1

        return output