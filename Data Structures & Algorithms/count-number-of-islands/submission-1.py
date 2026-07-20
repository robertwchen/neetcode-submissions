# where am I
    # at some point on grid
# what am I doing
    # checking if node visited or  is land then dfs
# what do I return
    # return # islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pos = (i, j)
                if pos not in visited and grid[i][j] == '1':
                    self.dfs(grid, i, j, visited)
                    count += 1
        return count
    
    def dfs(self, grid, r, c, visited):
        stack = [ (r, c) ]

        while stack:
            current_pos = stack.pop()
            r, c = current_pos
            visited.add(current_pos)

            for neighbor in self.valid_moves(r, c, grid):
                newR, newC = neighbor
                if neighbor not in visited and grid[newR][newC] != '0':
                    stack.append(neighbor)
        return
    
    def valid_moves(self, r, c, grid):
    
        moves = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
        
        def in_bounds(grid, r, c):
            row_in_bounds = 0 <= r < len(grid)
            col_in_bounds = 0 <= c < len(grid[0])
            return row_in_bounds and col_in_bounds

        valid_moves = []
        for move in moves:
            newR, newC = move
            if in_bounds(grid, newR, newC):
                valid_moves.append(move)
        return valid_moves

grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

visited = set()
solution = Solution()
solution.dfs(grid, 0, 1, visited)



        
