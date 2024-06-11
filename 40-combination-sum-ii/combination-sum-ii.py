class Solution(object):

    def find_all_combinations(self,picked,arr,target,res,cur,i):

        n = len(arr)

        if target<0:
            return 

        if i>=n:

            if target==0:
                temp = []

                for ele in cur:
                    temp.append(ele)
                    
                res.append(temp)
            return

        if i == 0:
            cur.append(arr[i])
            self.find_all_combinations(True,arr,target-arr[i],res,cur,i+1) # picking 
            cur.pop()
        
        else:
            if(picked): # only for the first element we are not performing any check and directly picking
                cur.append(arr[i])
                self.find_all_combinations(True,arr,target-arr[i],res,cur,i+1) # picking 
                cur.pop()
                
            
            # for other index elements we are performing the check
            if(not picked and arr[i]!=arr[i-1]): # we are checking whether the previous index element in the array is 
                                # same as the current i pointed element in the array
                cur.append(arr[i])
                self.find_all_combinations(True,arr,target-arr[i],res,cur,i+1) # picking 
                cur.pop()


        self.find_all_combinations(False,arr,target,res,cur,i+1) # not picking 

        
        
        

    def combinationSum2(self, arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        arr.sort()

        self.find_all_combinations(False,arr,target,res,[],0)

        return res