class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache
        def stair(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return stair(i+1) + stair(i+2)
        return stair(0)

        