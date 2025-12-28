class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n  = len(nums)

        if n == 1:
            return nums[0]
        

        
        
        max_till_now = nums[0]
        min_till_now = nums[0]

        overall_max = nums[0]

        for i in range(1,n):
            cur_max = max(max_till_now*nums[i],min_till_now*nums[i],nums[i])
            cur_min = min(min_till_now*nums[i],max_till_now*nums[i],nums[i])

            max_till_now = cur_max
            min_till_now = cur_min

            overall_max = max(overall_max,max_till_now)

        return overall_max
        


        