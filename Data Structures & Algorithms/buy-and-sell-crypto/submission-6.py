class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice =prices[0]
        for price in prices:
            minprice = min(minprice,price)
            profit =max(profit, price-minprice)
        return profit