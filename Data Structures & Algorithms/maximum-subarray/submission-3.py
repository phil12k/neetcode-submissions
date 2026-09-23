class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = 0
        res = nums[0]

        for num in nums:
            cur_max = max( cur_max + num, num)
            res = max(res, cur_max)

        return res
        
        