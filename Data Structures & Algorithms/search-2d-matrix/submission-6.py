class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Goal: find target in array
        # Store: p1 p2 
        # Valid: if target found, target found in right rown then right column
        # Fix: find correct array then find correct element if not early return
        # Answer: if find in row look column if not in column return false

        # First find row:
        p1 = 0
        p2 = len(matrix) - 1 # num arrays
        row = 0
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if target < matrix[mid][0]:
                p2 = mid - 1
            elif target > matrix[mid][-1]:
                p1 = mid + 1
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            else:
                return False
        

        
        p1 = 0
        p2 = len(matrix[0]) - 1
        while p1 <= p2:
            print(mid)
            mid = (p1 + p2) // 2
            if target < matrix[row][mid]:
                p2 = mid - 1
            elif target > matrix[row][mid]:
                p1 = mid + 1
            elif target == matrix[row][mid]:
                return True
        print("not found")
        return False
        