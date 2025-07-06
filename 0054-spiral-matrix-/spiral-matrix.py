from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = [] 

        top = 0
        left = 0
        bottom = len(matrix) - 1  #row of matrix 
        right = len(matrix[0]) - 1 #column

        while top <= bottom and left <= right:
            # move left to right
            for i in range (left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # move top to bottom(from rigth column)
            for i in range (top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1   

            # move right to left (across the bottom)
            if top <= bottom:
                for i in range (right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # move bottom to top (left column up)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result