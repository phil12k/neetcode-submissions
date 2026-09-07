class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min,cur_max =1,1
        res = nums[0]

        for num in nums:
            temp = cur_max*num
            cur_max  = max(cur_min*num, cur_max*num, num )
            cur_min = min(cur_min*num, temp, num)
            res = max(cur_max,res)

        return res

      


        

            