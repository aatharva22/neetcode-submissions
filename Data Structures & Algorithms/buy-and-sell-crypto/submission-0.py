class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]
        best = 0

        for i in range(1,len(prices)):

            minimum = min (prices[i],minimum)
            profit = prices[i] - minimum
            best = max(profit,best)
        
        return best