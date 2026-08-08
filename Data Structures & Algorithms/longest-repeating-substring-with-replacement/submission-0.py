class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        maxFreq = 0
        longest = 0


        for right in range(len(s)):
            # Expand the window
            count[s[right]] = count.get(s[right],0)+1
            
            #update the freq
            maxFreq = max( maxFreq , count[s[right]] )
            
            #if more replacements is needed, shrink the window
            while (right - left + 1 ) - maxFreq > k:
                count[s[left]]-=1
                left+=1
            
            #current window is valid
            longest = max(longest, right - left + 1)

        return longest

            

        