class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = 0
        prev = prices[0]
        diff = 0

        for price in prices[1:]:
            diff = price - prev

            current = max(0, current + diff)
            profit = max(profit, current)
            
            prev = price
        return profit