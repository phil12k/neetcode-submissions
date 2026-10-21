class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq1={}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1

            
        for right in range(len(t)):
            freq1[t[right]] = freq1.get(t[right],0)+1

        return freq==freq1
        

        

        
        