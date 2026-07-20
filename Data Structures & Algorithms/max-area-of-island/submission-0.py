# where am I
    # at some point on graph
# what am I doing
    # dfs a grpah to find the max size
# what do I return
    # max_size of island


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    current_size = self.dfs(grid, i, j, visited)
                    max_size = max(max_size, current_size)
        return max_size
    
    def dfs(self, grid, r, c, visited):
        stack = [ (r, c)]
        visited.add((r, c))     
        current_size = 0
        while stack:
            pos = stack.pop()
            current_size += 1
            r, c = pos
            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for move in moves:
                dR, dC = move
                if ((0 <= dR < len(grid)) and (0 <= dC < len(grid[0]))) and (move not in visited) and (grid[dR][dC] == 1):
                    stack.append((dR, dC))
                    visited.add((dR, dC))
        return current_size




