# where am I 

# what am I doing

# what do I return

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, i, visited):
            if i >= len(word):
                return True

            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited:
                return False

            if board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            # exlpore every possble path
            moves = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for move in moves:
                new_r, new_c = move
                if dfs(new_r, new_c, i + 1, visited):
                    return True

            visited.remove((r, c))

            return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, set()):
                    return True


        return False


    
   

        

        