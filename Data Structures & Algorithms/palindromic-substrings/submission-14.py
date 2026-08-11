class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]

        ans = 0

        #check single char
        for i in range(n):
            ans+=1
            dp[i][i]=True
        
        #check for 2 char of len
        for i in range(n-1):
            if s[i]==s[i+1]:
                ans+=1
                dp[i][i+1]=True
        
        #check for 3 char or more
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = length + i - 1

                if s[i]==s[j] and dp[i+1][j-1]:
                    ans+=1
                    dp[i][j]=True
        return ans
