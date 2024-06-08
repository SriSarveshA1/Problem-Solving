class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        min_len = pow(10,8)
        n = len(nums)

        cur_sum = 0

        flag = False
        while r<n:
            cur_sum+=nums[r]

            while(cur_sum>=target):
                flag = True
                length = (r-l)+1
                min_len = min(length,min_len)

                cur_sum-=nums[l]
                l+=1
            
            r+=1
        
        if flag:
            return min_len
        
        return 0