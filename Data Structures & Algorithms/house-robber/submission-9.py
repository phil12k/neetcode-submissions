class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache
        @cache
        
        #copied ={}
        def dfs(i):
            if i>=len(nums):
                return 0
            #    if i in copied:
            #    return copied[i]
            rob = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            #copied[i] = max(rob,skip)
            return max(rob,skip)

        return dfs(0)


        
        