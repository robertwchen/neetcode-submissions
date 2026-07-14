class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count_rows = set()
        for i in range(0, len(grid)):
            current = 0
            count_rows_temp = set()
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    count_rows_temp.add((i, j))
                    current += 1
            if current == 1:
                continue
            count_rows = count_rows_temp | count_rows

        count_cols = set()
        for j in range(0, len(grid[0])):
            current = 0
            count_cols_temp = set()
            for i in range(0, len(grid)):
                if grid[i][j] == 1:
                    count_cols_temp.add((i, j))
                    current += 1
            print(j, current)
            if current == 1:
                continue
            count_cols = count_cols_temp | count_cols

        return len(count_cols | count_rows)
        # go through all columns
            # count 1s in each row
            # if count == 1 and not in counted then remove()
            #
        