class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        minimum = prices[0]

        for i in range(1, len(prices)):
            minimum = min(minimum, prices[i])
            best = max(prices[i]-minimum, best)
            
            
        return best