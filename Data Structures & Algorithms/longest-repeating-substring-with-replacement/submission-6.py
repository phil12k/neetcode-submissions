class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        n = len(s)
        left = 0
        maxFreq = 0

        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1
            maxFreq = max(maxFreq,freq[s[right]])

            while right - left + 1 - maxFreq >k:
                freq[s[left]]-=1
                left+=1
            
            longest = max(longest, right - left + 1) 
        return longest
                





