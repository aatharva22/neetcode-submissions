class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while (left < right ) :

            # Moving which has less height, as the width decreases in any case by 1
            #But the less height is the one which calculates the area, if the more height
            # pointer is moved, we might lose a solution, as what if the next left had more 
            # or equal height than the right, by moving right we lose that case.
            area = min(heights[left], heights[right]) * (right - left )
            maxArea = max(maxArea, area)
            if heights[left] < heights[right]:
                left += 1
            else : 
                right -= 1
        
        return maxArea