class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        
        
        if len(nums)==1:
            return nums[0]
        
         
        def robLinear(houses):
            @cache
            def dfs(i):
                if i>= len(houses):
                    return 0
                rob = houses[i]+ dfs(i+2)
                skip = dfs(i+1)
                return max(rob, skip)
            return dfs(0)
            

        return max(robLinear(nums[1:]),robLinear(nums[:-1]))
        



        

