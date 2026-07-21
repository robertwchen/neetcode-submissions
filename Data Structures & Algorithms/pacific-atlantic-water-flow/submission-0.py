class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        queue = deque([])
        for r in range(0,len(heights)):
            queue.append((r, 0))
            pacific_set.add((r, 0))
        for c in range(len(heights[0])):
            queue.append((0, c))
            pacific_set.add((0, c))
        while queue:
            r, c = queue.popleft()
            height = heights[r][c]
            moves = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for move in moves:
                newR, newC = move
                if not self.inrange(heights, newR, newC):
                    continue
                if heights[newR][newC] >= heights[r][c]:
                    if (newR, newC) in pacific_set:
                        continue
                    pacific_set.add((newR, newC))
                    queue.append((newR, newC))
        

        atlantic_set = set()
        queue = deque([])
        for r in range(0,len(heights)):
            queue.append((r, len(heights[0]) - 1))
            atlantic_set.add((r, len(heights[0]) - 1))
        for c in range(len(heights[0])):
            queue.append((len(heights) - 1, c))
            atlantic_set.add((len(heights[0]) - 1, c))
        while queue:
            r, c = queue.popleft()
            height = heights[r][c]

            moves = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for move in moves:
                newR, newC = move
                if not self.inrange(heights, newR, newC):
                    continue
                if heights[newR][newC] >= heights[r][c]:
                    if (newR, newC) in atlantic_set:
                        continue
                    atlantic_set.add((newR, newC))
                    queue.append((newR, newC))
        both_set = atlantic_set & pacific_set
        
        result = []
        for pos in both_set:
            r, c = pos
            result.append([r, c])
        return result
        #for location in both_set:
            

    
    def inrange(self, grid, r, c):
        r_inrange = 0 <= r < len(grid)
        c_inrange = 0 <= c < len(grid[0])
        return r_inrange and c_inrange
            