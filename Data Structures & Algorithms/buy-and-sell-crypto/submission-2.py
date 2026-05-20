class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = prices[len(prices)-1]
        best = 0

        # Moving left to right, might lost the cheapest price to buy stock
        # so saving the minimum price, and the best profit
        # as moving left to right the buying price(minimum) is always < selling price
        for i in range(len(prices)-2, -1, -1):

            maximum = max (prices[i],maximum)
            profit = maximum - prices[i]
            best = max(profit,best)
        
        return best