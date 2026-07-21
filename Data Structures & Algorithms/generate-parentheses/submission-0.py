# where am I
    # 
# what am I doing
# what do I return

# [()]
# (()) #()()
# ()(()) (())() ()()()

# )(
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        comb = []
        def dfs(open_count, close_count):
            if open_count == n and close_count == n:
                result.append("".join(comb))
                return

            # open door
            if open_count < n:
                comb.append('(')
                dfs(open_count + 1, close_count)
                comb.pop()
            if close_count < open_count:
                comb.append(')')
                dfs(open_count, close_count + 1)
                comb.pop()
        dfs(0, 0)
        return result


            # close door
        