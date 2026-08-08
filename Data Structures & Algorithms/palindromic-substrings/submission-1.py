class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]

        answer = 0
        
        for i in range(n):
            dp[i][i]=True
            answer+=1


        for i in range(n-1):
            j = i+1
            if s[i] == s[j]:
                dp[i][j]=True
                answer +=1  

        for length in range(3, n + 1):
            for i in range(n - length + 1 ):
                j = i + length - 1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]= True
                    answer+=1
        return answer


        