class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        
        if len(nums)==1:
            return nums[0]
        
        def robber(house):
            @cache
            def dfs(i):
                if i>=len(house):
                    return 0
                rob = house[i]+dfs(i+2)
                skip = dfs(i+1)
                return max(rob, skip)
            return dfs(0)


        return max(robber(nums[1:]),robber(nums[:-1]))