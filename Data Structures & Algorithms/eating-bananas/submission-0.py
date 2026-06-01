class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        def check(speed) -> bool:
            time = 0
            for pile in piles:
                time += -(-pile//speed)
            if time <= h:
                return True
            return False
        
        left = 1
        right = max(piles)
        k = 0
        while left < right:
            mid = (left + right ) // 2

            if check(mid):
                k = mid
                right = mid 
            elif not check(mid):
                left = mid + 1
        return left

