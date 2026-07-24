class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        
        def dfs(r , c, memo):
            key = (r, c)
            if key in memo:
                return memo[key]
            if r == m - 1 and c == n - 1:
                return 1
            
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            print(r, c)
            
            right = dfs(r, c + 1, memo)
            down = dfs(r + 1, c, memo)
            memo[key] = down + right
            return memo[key]

        return dfs(0, 0, {}) 
# m = 1, n = 1