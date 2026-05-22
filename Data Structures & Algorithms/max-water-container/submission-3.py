class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #choice to make, move small one or larger one,
        #area now is determined by the height of small
        #if larger is moved, 
        #and next one is even larger then still area is determined
        # by height of small(same area), 
        # if the next one is smaller than the small, area is determined by 
        #height of smaller, we get even less area
        #in this case we lost the large, what if we had moved small, and found a 
        #larger element, then the area would be according to large, 

        #case2:- if small is moved, and next element is larger than the large
        #then area is determined by the large element(more area), and if the next 
        #element is smaller than small, we get less area(but we have preserved the
        # large which can give area according to its height)

        #move ahead with case 2 

        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:

            area = (right - left) * (min(heights[left],heights[right]))
            maxWater = max(area, maxWater)

            if heights[left] < heights[right]:
                left += 1
            else :
                right -= 1
            
        return maxWater
            



