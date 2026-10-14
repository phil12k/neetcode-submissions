class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()
        missing =1
        
        for num in nums:
            if num<missing:
                continue
            
            elif num == missing:
                missing+=1
            
            else:
                return missing 
        return missing