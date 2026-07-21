class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find all 1s:
        queue = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, distance = queue.popleft()
            
            if grid[r][c] != 0: 
                grid[r][c] = distance
                visited.add((r, c))

            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for move in moves:
                newR, newC = move
                if (move not in visited) and (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])) and grid[newR][newC] != -1:
                    queue.append((newR, newC, distance + 1))
                    visited.add((newR, newC))
        return




        
        