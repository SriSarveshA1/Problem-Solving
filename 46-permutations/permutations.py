class Solution(object):

    def generate_permutations(self,n,nums,picked_arr,cur,res):

        if len(cur) == n:

            # now add this cur to res
            temp = []
            for ele in cur:
                temp.append(ele)
            
            res.append(temp)
            return
        
        for i in range(0,n):
            # Try to mark each 'i' as picked and then call for the next recursion
            if picked_arr[i]:
                continue
            
            cur.append(nums[i])
            picked_arr[i]=True
            self.generate_permutations(n,nums,picked_arr,cur,res)
            picked_arr[i]=False
            cur.pop()



    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur = []
        res = []
        n = len(nums)
        picked_arr = [False for i in range(n)]
        self.generate_permutations(n,nums,picked_arr,cur,res)
        return res

        