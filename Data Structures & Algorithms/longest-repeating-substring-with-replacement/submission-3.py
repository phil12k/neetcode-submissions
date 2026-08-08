class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        maxFreq = 0
        long = 0
        
        for right in range(len(s)):
            #add char
            freq[s[right]] = freq.get(s[right] , 0) + 1
            #search for maxFreq
            maxFreq = max(maxFreq,freq[s[right]])
            #while the lenght of window - maxfreq <=k you can exapnd the window
            while (right - left + 1) - maxFreq> k:
                freq[s[left]] = freq.get(s[left] , 0) - 1
                left+=1
            long = max(long, right - left + 1) 
            #update ans
        return long






