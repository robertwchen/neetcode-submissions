# where am I
# what am I doing
# what do I return


# [[]]
# [1, 2, 3 ,4].   # 0
# [5, 6, 7, 8].   # 1
# [9, 10, 11, 12] # 2

# [[1, 2, 3]] # 0


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        # find the row first
        lo = 0
        hi = len(matrix) - 1
        row = -1
        while lo <= hi:
            mid = (hi + lo) // 2
            if target > matrix[mid][-1]: 
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                row = mid
                break
        print(lo, hi)
        if row == -1:
            return False
        
        lo = 0
        hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if target > matrix[row][mid]:
                lo = mid + 1
            elif target < matrix[row][mid]:
                hi = mid - 1
            else:
                return True
        return False

        

                


