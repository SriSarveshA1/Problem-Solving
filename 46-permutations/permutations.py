class Solution(object):

    def return_first_matching_availble_idx(self,n, picked_arr):
        for idx in range(0,n):
            if not picked_arr[idx]:
                return idx
        return -1

    def generate_paranthesis(self,nums,cur,res,picked_arr):
        n = len(nums)
        if len(cur) == n:
            res.append(cur[:])
            return
        
        for i in range(0,n):
            if picked_arr[i]:
                continue
            
            picked_arr[i] = True
            cur.append(nums[i])
            self.generate_paranthesis(nums,cur,res,picked_arr)
            cur.pop()
            picked_arr[i] = False
        

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        picked_arr = [False for i in nums]
        self.generate_paranthesis(nums,[],res,picked_arr)
        return res
