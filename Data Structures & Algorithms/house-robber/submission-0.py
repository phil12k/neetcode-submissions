class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(i):
            if i>=size:
                return 0
            rob = nums[i]+dfs(i+2)
            skip =dfs(i+1)
            return max(rob,skip)
        size=len(nums)
        return dfs(0) 
        