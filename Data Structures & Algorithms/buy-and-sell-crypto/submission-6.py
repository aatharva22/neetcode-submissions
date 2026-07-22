class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minV = prices[0]

        for p in prices:

            profit = max(profit,(p-minV))

            minV = min(minV, p)
        
        return profit