class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        long = 0
        start =0
        dp = [[False]*n for i in range(n)]
        
        # one char
        for i in range(n):
            dp[i][i]=True
            long = max(long,1)
        #two char
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                long=max(long,2)
                if 2>=long:
                    start = i
                    long = 2
        #three char or more
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = length + i -1
                if s[i]==s[j] and dp[i+1][j-1]:
                    if length > long:
                        start = i
                        long = length
                    #long = max(long,j-i+1)
                    dp[i][j]= True



        return s[start:start+long]

        