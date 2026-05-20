class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = prices[len(prices)-1]
        best = 0

        # Moving  right to left , might lost the max selling price to sell stock
        # so saving the maximum price, and the best profit
        # as moving right to left the selling price(maximum) is always after buying price
        for i in range(len(prices)-2, -1, -1):

            maximum = max (prices[i],maximum)
            profit = maximum - prices[i]
            best = max(profit,best)
        
        return best