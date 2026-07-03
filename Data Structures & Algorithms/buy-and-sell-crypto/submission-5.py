class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minimum = prices[0]

        for price in prices:
            profit = price - minimum
            minimum = min(price , minimum)
            maxProfit = max(profit,maxProfit)
        return maxProfit