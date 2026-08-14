class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        long = 0
        n = len(s)
        dp = [[False]*n for i in range(n)]

        #one char palindrome
        for i in range(n):
            dp[i][i]=True
            #start = i
            long = 1

        #two char palindrom
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]= True
                if 2 > long:
                    start= i
                    long = 2

        #three char palindrome
        for length in range( 3 , n + 1 ):
            for i in range(n + 1 - length ):
                j = length -1 + i 
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    if length> long :
                        start = i
                        long = max(long,length)
        return s[start:start+long] 