class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_len = 0

        for ele in nums:
            
            if (ele-1) not in nums:

                cur_len = 0
                temp = ele
                while (temp in nums):
                    cur_len += 1
                    temp = temp+1
                
                max_len = max(cur_len,max_len)
        
        return max_len
