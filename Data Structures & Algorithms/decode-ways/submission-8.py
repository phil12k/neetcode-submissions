class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 1
            if s[i]=="0":
                return 0
        #take 1 digit
            ways = dfs(i+1)
        #take 2 digits for double digit
            if (i+1) < n and 10<= int(s[i:i+2]) <=26:
                ways += dfs(i+2)            
            return ways

        return dfs(0)
        