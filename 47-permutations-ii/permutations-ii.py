class Solution(object):
    def generate_paranthesis(self,nums,cur,res,picked_arr):
        n = len(nums)
        if len(cur) == n:
            res.append(cur[:])
            return
        
        for i in range(0,n):
            # checking for duplicates
            if (i>0 and nums[i-1]==nums[i] and not picked_arr[i-1]):
                continue

            if picked_arr[i]:
                continue
            
            picked_arr[i] = True
            cur.append(nums[i])
            self.generate_paranthesis(nums,cur,res,picked_arr)
            cur.pop()
            picked_arr[i] = False
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        picked_arr = [False for i in nums]
        self.generate_paranthesis(nums,[],res,picked_arr)
        return res
        