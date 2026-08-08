class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        size = len(nums)
        #@cache
        copied={}
        def dfs(i):
            if i>=size:
                return 0
            if i in copied:
                return copied[i]
            
            rob = nums[i]+dfs(i+2)
            skip = dfs(i+1)
            copied[i]=max(rob, skip)
            return copied[i]

        return dfs(0)