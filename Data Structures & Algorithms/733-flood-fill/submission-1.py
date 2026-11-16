class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Time complexity: Worst case O(m * n)
        # Space complexity: Create structure of visited sites O(m * n)
        # m = len(image), n = len(image[0])

        # Edge cases
        # Main code
        def recursive(r, c, visited):
            if 0 > r or r >= m or 0 > c or c >= n: return # Outside image
            if visited[r][c]: return # Already visited, go back

            # New place, mark it as visited
            visited[r][c] = True
            if image[r][c] != color_to_flood: 
                # Nothing to do here
                return
            
            # Change color and explore N, S, W, E
            image[r][c] = color
            recursive(r+1, c,   visited) # N
            recursive(r-1, c,   visited) # S
            recursive(r,   c-1, visited) # W
            recursive(r,   c+1, visited) # E
                
        # Create a 2D structure to mark visited locations
        m = len(image)
        n = len(image[0])
        visited = [[False] * n for _ in range(m)]        
        # Start from the provided source point
        color_to_flood = image[sr][sc] 
        recursive(sr, sc, visited)
        return image