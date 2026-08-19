class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache

        def climbed(i):

            if i > n:
                return 0
            if i ==n:
                return 1 
      
            return climbed(i+1) + climbed(i+2)



        return climbed(0)