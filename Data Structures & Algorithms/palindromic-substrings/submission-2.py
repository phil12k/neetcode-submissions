class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False]*n for i in range(n)]
        
        #base case 1
        for i in range(n):
            ans+=1
            dp[i][i]=True

        #base case 2
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                ans+=1

        #base case for 3 char or more
        for length in range(3,n+1):
            for i in range(n- length +1):
                j = length + i -1
                if s[i]==s[j] and dp[i+1][j-1]:
                    ans+=1
                    dp[i][j]=True
        return ans
