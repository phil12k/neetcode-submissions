class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        maxfreq = 0
        frq ={}

        for right in range(len(s)):
            frq[s[right]] = frq.get( s[right], 0 ) + 1
            maxfreq = max(maxfreq, frq[s[right]])
            while right - left + 1 - maxfreq > k:
                frq[s[left]] -=1
                left+=1
            longest = max(longest,right -left+1)
        return longest
