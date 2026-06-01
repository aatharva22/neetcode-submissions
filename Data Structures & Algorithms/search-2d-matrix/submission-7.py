class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0 
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        while top <= bottom:
            midRow = (top + bottom) // 2

            if target > matrix[midRow][right]:
                top = midRow + 1
            elif matrix[midRow][0]<= target <= matrix[midRow][right]:
                if target == matrix[midRow][0] or target == matrix[midRow][right]:
                    return True
                top = midRow
                break
            elif target < matrix[midRow][right]:
                bottom = midRow - 1
                
        left = 0
        while left <= right and top < len(matrix):
            mid = (left + right) // 2

            if target > matrix[top][mid]:
                left = mid + 1
            elif target < matrix[top][mid]:
                right = mid - 1
            else:
                return True
        return False

