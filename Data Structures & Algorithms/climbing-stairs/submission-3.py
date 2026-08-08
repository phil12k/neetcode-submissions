class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        #@cache
        seen ={}
        def climb(i):
            if i in seen:
                return seen[i]
            if i>n:
                return 0
            if i == n:
                return 1
            seen[i] =  climb(i+1)+climb(i+2)

            return seen[i]
        

        return climb(0)