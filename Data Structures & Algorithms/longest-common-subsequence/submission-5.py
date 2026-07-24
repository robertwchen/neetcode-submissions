class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dfs(p1, p2, memo):
            key = (p1, p2)
            if key in memo:
                return memo[key]

            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if text1[p1] == text2[p2]:
                memo[key] = 1 + dfs(p1 + 1, p2 + 1, memo)# try with p1 + 1, p2 + 1
                return memo[key]

            else:
                try_again = dfs(p1, p2 + 1, memo)
                skip = dfs(p1 + 1, p2, memo)
                memo[key] = max(try_again, skip)
                return memo[key]
            
                # try p1, p2 + 1
                # try p1 + 1, p2 + 1
        return dfs(0, 0, {})
                

    
