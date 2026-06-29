class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for x in prices:
            if x < lowest_price:
                lowest_price = x
            
            profit = x - lowest_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


            