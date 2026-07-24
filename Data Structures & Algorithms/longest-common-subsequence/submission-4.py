class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1 = len(text1)
        len_2 = len(text2)

        if len_1 > len_2:
            longer = text1
            shorter = text2
        else:
            longer = text2
            shorter = text1

        # cat        # crabt
        # p1          #p2

        def dfs(p1, p2, memo):
            key = (p1, p2)
            if key in memo:
                return memo[key]
            if p2 >= len(longer) or p1 >= len(shorter):
                return 0

            if shorter[p1] == longer[p2]:
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
                

    
