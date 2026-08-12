class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache
        n = len(s)

        @cache
        def dfs(i):
            #reached end of string
            if i == n:
                return 1
           
           
            #base case 1: no didgit cant be decode
            if s[i] == "0":
                return 0
            
            ways = dfs(i + 1)

            #base case 2: for double digits
            # Take two digits
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            return ways

        return dfs(0)
        