class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxV = prices[len(prices) - 1]

        best = 0

        for i in range(len(prices ) - 1, -1, -1):

            best = max(best, maxV - prices[i]) 

            maxV = max(maxV, prices[i])
        return best 