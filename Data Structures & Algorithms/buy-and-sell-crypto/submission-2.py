class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        maximum_profit = 0

        for x in prices:
            if x < minimum_price:
                minimum_price = x
            
            profit = x - minimum_price
            
            if profit > maximum_profit:
                maximum_profit = profit
        
        return maximum_profit
            