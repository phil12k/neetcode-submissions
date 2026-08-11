class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache
        size = len(nums)
        @cache
        def robber(i):
            if i>= size:
                return 0
            rob = nums[i] + robber(i+2)
            skip = robber(i+1)

            return max(rob, skip)


        return robber(0)