class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def check(speed) -> bool:
            time = 0
            for pile in piles:
                time +=  -(- pile // speed)
            if time <= h:
                return True
            return False
        
        #speed range can be in 1 and max(piles)

        right = max(piles)
        left = 1
        

        while right > left:

            mid = (right + left) // 2

            if check(mid):

                right = mid 
            
            else:
                left = mid + 1
        
        return left
