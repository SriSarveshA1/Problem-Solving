class Solution(object):

    def is_prev_element_same(self,nums,i):

        if i==0:
            return False
        
        if nums[i-1] == nums[i]:
            return True

    def generate_subs(self,nums,cur,res,i,is_picked):
        nums.sort()
        n = len(nums)

        if i>=n:
            temp = []
            for v in cur:
                temp.append(v)
            
            res.append(temp)
            return

        if is_picked==True or not self.is_prev_element_same(nums,i):
            cur.append(nums[i])
            self.generate_subs(nums,cur,res,i+1,True)
            cur.pop()

        

        self.generate_subs(nums,cur,res,i+1,False)
        
        

       


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]   
        :rtype: List[List[int]]
        """
        res = []
        self.generate_subs(nums,[],res,0,True)
        return res
        