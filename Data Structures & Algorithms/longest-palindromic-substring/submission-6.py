class Solution:
    def longestPalindrome(self, s: str) -> str:
        n =len(s)
        start = 0
        dp=[[False]*n for i in range(n)]
        longest =0

        #one char palindrome check
        for i in range(n):
            dp[i][i]=True
            longest =1

        #two char palindrome check
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                if 2>=longest:
                    longest = max(longest,2)
                    start = i
        #three char pal check
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = length + i - 1
                if s[i]==s[j] and dp[i+1][j-1]:
                    if length >= longest:
                        start = i
                        longest = length
                    dp[i][j]=True
        return s[start:start+longest]
