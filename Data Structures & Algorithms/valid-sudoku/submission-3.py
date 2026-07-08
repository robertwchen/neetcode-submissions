from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set) # key will be (row - col)

        # loop through each element
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                val = board[i][j]
                
                if val == '.':
                    continue
                
                if val in row_map[i]:
                    return False
                if val in col_map[j]:
                    return False
                if val in square_map[(i // 3, j // 3)]:
                    # print(val, "square_num",(i // 3, j // 3), square_map[(i // 3, j // 3)])
                    return False
                
                row_map[i].add(val)
                col_map[j].add(val)
                square_map[(i // 3, j // 3)].add(val)
        return True








        


         

        