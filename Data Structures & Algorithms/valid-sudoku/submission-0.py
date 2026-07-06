from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every row create row counter {1: set() 2: set() }
        # for every colum create colunn counter (1: set(), 2: set()}
        # for every square create set

        # check square function -> returns true or false, if true set square 1:9
        row_map = defaultdict(set)
        column_map = defaultdict(set)
        square_map = defaultdict(set)


        def check_row(i, j):
            if board[i][j] in row_map[i]:
                return False
            row_map[i].add(board[i][j])
            return True
            
            
        def check_column(i, j):
            if board[i][j] in column_map[j]:
                return False
            column_map[j].add(board[i][j])
            return True

        def find_square(i, j):
            simp_i = i // 3
            simp_j = j // 3

            if simp_i == 0:
                if simp_j == 0:
                    return 0
                if simp_j == 1:
                    return 1
                if simp_j == 2:
                    return 2
            if simp_i == 1:
                if simp_j == 0:
                    return 3
                if simp_j == 1:
                    return 4
                if simp_j == 2:
                    return 5
            if simp_i == 2:
                if simp_j == 0:
                    return 6
                if simp_j == 1:
                    return 7
                if simp_j == 2:
                    return 8
            return None


        def check_square(i, j):
            square_num = find_square(i,j)
            if board[i][j] in square_map[square_num]:
                return False
            square_map[square_num].add(board[i][j])
            return True

        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if not check_row(i, j):
                    return False
                if not check_column(i, j):
                    return False
                if not check_square(i, j):
                    return False
        return True






        


         

        