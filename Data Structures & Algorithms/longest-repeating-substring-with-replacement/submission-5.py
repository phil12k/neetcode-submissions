class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        maxFreq = 0
        left = 0

        #expand the sliding window
        for right in range(len(s)):
            #add freq of char
            freq[s[right]] = freq.get(s[right],0) + 1
            #track the highest freq
            maxFreq = max(maxFreq, freq[s[right]])
            #check the invarient
            #shrink the window if more k replacement is needed
            while (right - left + 1) - maxFreq > k:
                freq[s[left]]-=1
                left+=1
            #window is valid , update the longest answer
            longest = max(longest, right - left+1)
        return longest
                





