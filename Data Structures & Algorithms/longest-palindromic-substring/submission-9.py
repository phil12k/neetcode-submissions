class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        long=0
        n = len(s)
        dp = [[False]*n for i in range(n)]

        #one char dp
        for i in range(n):
            dp[i][i]=True
            long = 1

        #2 char dp
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                if long< 2:
                    long = 2
                    start = i
        
        #3 char dp
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = length + i - 1
                if s[i]==s[j] and dp[i+1][j-1]:
                    if length > long:
                        start = i
                        long = max(long, length) 
                    dp[i][j]=True
        return s[start:start+long]
