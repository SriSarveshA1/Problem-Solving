class Solution(object):
    def is_prev_element_same(self,nums,i):
        if i==0:
            return False
        
        if nums[i-1] == nums[i]:
            return True

    def generate_subs(self,nums,cur,res,i,is_picked,target):
        n = len(nums)

        if i>=n or target<0:
            if target == 0:
                temp = []
                for v in cur:
                    temp.append(v)
                
                res.append(temp)

            return

        if is_picked==True or not self.is_prev_element_same(nums,i):
            cur.append(nums[i])
            self.generate_subs(nums, cur, res, i+1, True, target-nums[i])
            cur.pop()

        
        self.generate_subs(nums, cur, res, i+1, False, target)
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=candidates
        nums.sort() # Sorting the numbers in asc order so that the duplicate numbers comes first

        res = []

        self.generate_subs(nums,[],res,0,True,target)
        
        return res