class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        long = 0
        count ={}
        maxFreq = 0

        for right in range(len(s)):
            #expand window
            count[s[right]]=count.get(s[right],0)+1
            #update freq
            maxFreq = max(maxFreq, count[s[right]])

            # formula
            if ( right - left + 1 ) - maxFreq > k:
                #shrink window
                count[s[left]]-=1
                left+=1
            long = max(long,right-left+1)
        return long


        