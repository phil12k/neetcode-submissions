class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache
        size = len(cost)
        price = 0
        @cache
        def climb(i):
            if i >= size:
                return 0

            return cost[i] + min( climb(i+1) , climb(i+2) )

        return min(climb(0),climb(1))
        