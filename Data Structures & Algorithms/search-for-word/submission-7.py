# where am I
    # at some letter
# what am I doing
    # look for first letter
# what do I return
    # when found the string

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i]:
                return False
            if (r, c) in visited:
                return False

            visited.add((r, c))

            result = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs( r, c - 1, i + 1)

            visited.remove((r, c))
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False


            
            
            
            
            # try a cell
            # add it to visited

