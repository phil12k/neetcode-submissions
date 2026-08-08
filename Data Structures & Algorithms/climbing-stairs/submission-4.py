class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        #@cache
        memo ={}
        def climb(i):
            if i in memo:
                return memo[i]
            if i>n:
                return 0
            if i == n:
                return 1
            memo[i] =  climb(i+1)+climb(i+2)

            return memo[i]
        

        return climb(0)