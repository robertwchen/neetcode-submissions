# where am I
    # at some point on the grid
# what am I doing
    # I bfs with unique visited cell for each treasure and then turn that land into number 
# what do I return
    # return the same grid but modified
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == -1 or grid[r][c] == 0:
                    continue
                
                grid[r][c] = self.bfs(grid, r, c, set())
                
        # check < float('inf')
        return

    def bfs(self, grid, r, c, visited):
        queue = deque([(r, c, 0)])
        visited.add((r, c))

        while queue:
            r, c, distance = queue.popleft()
            
            if grid[r][c] == 0:
                return distance
            
            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for move in moves:
                new_r, new_c = move
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != -1:
                    if move not in visited:
                        queue.append((new_r, new_c, distance + 1))
                        visited.add((new_r, new_c))

        print("failed")
        return float('inf')



