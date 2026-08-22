class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        if len(nums)==1:
            return nums[0]

        def dfs(house):

            
            @cache
            def linearDfs(i):
                if i >= len(house):
                    return 0
                rob = house[i] + linearDfs(i+2)
                skip = linearDfs(i+1)

                return max(rob , skip)


            return linearDfs(0)       


        return max(dfs(nums[1:]),dfs(nums[:-1]))

