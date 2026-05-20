class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]
        best = 0

        # Moving left to right, might lost the cheapest price to buy stock
        # so saving the minimum price, and the best profit
        # as moving left to right the buying price(minimum) is always < selling price
        for i in range(1,len(prices)):

            minimum = min (prices[i],minimum)
            profit = prices[i] - minimum
            best = max(profit,best)
        
        return best