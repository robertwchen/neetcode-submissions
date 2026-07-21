# where am I
    # at all rotting bananas
# what am I doing
    # processing all bananas
# what do I return
    # time it takes

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        no_bananas = True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    no_bananas = False
        if no_bananas:
            return 0

        minutes = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                if grid[r][c] == 1:
                    grid[r][c] = 2
                print(r, c)
                
                moves = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
                for move in moves:
                    newR, newC = move
                    if not self.inbounds(grid, newR, newC):
                        continue
                    
                    if grid[newR][newC] == 0 or grid[newR][newC] == 2:
                        continue
                    
                    if move not in visited:
                        queue.append(move)
                        visited.add(move)
            minutes += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return minutes

    def inbounds(self, grid, r, c):
        r_inbounds = 0 <= r < len(grid)
        c_inbounds = 0 <= c < len(grid[0])

        return r_inbounds and c_inbounds
        