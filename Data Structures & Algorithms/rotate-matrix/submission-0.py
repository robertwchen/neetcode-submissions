class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1
        # 0, 1

        while l < r:
            for i in range(r - l):
                t, b = l, r

                temp = matrix[t][l + i] 
                #top left = bottom left
                matrix[t][l + i] = matrix[b - i][l]
                # bottom left = bottom right
                matrix[b - i][l] = matrix[b][r - i]

                # bottom right = top right
                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = temp
            l += 1
            r -= 1
