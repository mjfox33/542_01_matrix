import math
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0]) # assuming all rows have the same number of columns

        for row in range(m):
            for col in range(n):
                if mat[row][col] > 0:
                    top = mat[row-1][col] if row > 0 else math.inf
                    left = mat[row][col-1] if col > 0 else math.inf
                    mat[row][col] = min(top,left)+1
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if mat[row][col] > 0:
                    bottom = mat[row+1][col] if row < m-1 else math.inf
                    right = mat[row][col+1] if col < n-1 else math.inf
                    mat[row][col] = min(mat[row][col], bottom+1, right+1)
        return mat
