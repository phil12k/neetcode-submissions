class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache
        
        if len(nums)==1:
            return nums[0]
        
        
        def linear(arr):

            
            @cache
            def dfs(i):
                if i>=len(arr):
                    return 0
                
                skip = dfs(i+1)
                
                rob = arr[i]+dfs(i+2)
                
                return max(skip,rob)
            return dfs(0)


        return max(linear(nums[:-1]), linear(nums[1:]))
        