class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Super-slow version; checking all possibilities
        max = 0
        for day_buy in range(len(prices)-1):
            for day_sell in range(day_buy+1,len(prices)):
                if prices[day_sell] - prices[day_buy] > max :
                    max = prices[day_sell] - prices[day_buy]
        return max

