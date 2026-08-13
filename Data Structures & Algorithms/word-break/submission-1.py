class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                #len of each word in dict is less than string   --> cond 1
                #slicing the string with i and len of word == w --> cond 2
                if i + len(w)<= len(s) and s[i: i+len(w)] == w:
                    dp[i]=dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]

        