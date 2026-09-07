class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max,cur_min = 0,0
        res=nums[0]

        for num in nums:
            temp = cur_max + num
            cur_max = max( cur_min+num, cur_max + num, num )
            cur_min = min( cur_min+num, temp, num)
            res = max(res,cur_max)
        return res



        
        