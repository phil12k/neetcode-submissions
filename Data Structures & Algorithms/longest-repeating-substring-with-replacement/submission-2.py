class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set()
        left = 0
        long = 0
        count = {}
        freq = 0

        for right in range(len(s)):
            #create a window
            count[s[right]] = count.get( s[right], 0 ) + 1
            #update freq
            freq = max(freq, count[s[right]])
            #use the formula
            if ( right - left + 1 ) - freq > k :
                count[s[left]]-=1
                left+=1
            long = max(long,right-left+1)
        return long

