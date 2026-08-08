from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if len(t) > len(s):
            return ""
        # Frequency map of characters we need
        target = Counter(t)
       
        #freq map of current window
        window = {}
        
        #Number of unique character required to satisfy
        have = 0
        
        #total char needed to satisfy
        need= len(target)

        left = 0

        #store best answer
        minLength = float('inf')
        answer=""

        #expand windows

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0)+1

            #if char satisfy the count
            if char in target and window[char]==target[char]:
                have+=1

            #make window smaller
            while have ==need:
                currLength = right - left +1
                if currLength < minLength:
                    minLength = currLength
                    answer = s[left:right + 1]
                # remove left character
                leftChar = s[left]
                window[leftChar] -= 1
                #did removing leftchar in window make window invalid
                if leftChar in target and window[leftChar] < target[leftChar]:
                    have-=1
                #update left ptr position after removing left char
                left+=1

        return answer
            

            
