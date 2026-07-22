class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #so we can search the valid rate space
        #that is 1 to max(the array)

        k = max(piles)

        left = 1

        while left < k:

            mid = (left + k) // 2
            time = 0
            for p in piles:
                time += -(-p//mid)
            
            if time <= h:
                k = mid
            else:
                left = mid + 1
        
        return left

