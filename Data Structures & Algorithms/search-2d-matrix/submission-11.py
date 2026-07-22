class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #Find row
        #then in row find target

        col = len(matrix[0]) - 1
        row = len(matrix) - 1
        i = 0
        j = row
        
        while i < j:

            mid = (i + j) // 2

            if matrix[mid][col] < target:
                i = mid + 1
            else:
                j = mid
            
            # i is the row

        left = 0 
        right = col

        while left <= right:

            mid = (left + right) // 2

            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid - 1
            else:
                left += 1
        
        return False
        



