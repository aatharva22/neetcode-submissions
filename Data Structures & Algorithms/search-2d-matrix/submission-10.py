class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bottom = len(matrix) - 1
        top = 0
        target_row = -1

        while bottom >= top:

            mid = (bottom + top) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                target_row = mid
                break
        if target_row == -1:
            return False

        left = 0
        right = len(matrix[0]) -1 
        while left <= right:

            mid = (left + right ) // 2

            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                
                right = mid - 1
            else:
                return True
        
        return False
