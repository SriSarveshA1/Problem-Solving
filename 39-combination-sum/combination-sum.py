class Solution(object):
    
    def find_all_combinations(self,arr,res,cur,target,i):
        n = len(arr)

        if target<0:
            return 
        
        if i>=n:
            if target==0:
                temp=[]
                for ele in cur:
                    temp.append(ele)
                
                res.append(temp)

            return
        
        cur.append(arr[i])
        self.find_all_combinations(arr,res,cur,target-arr[i],i) #picking the element and not increasing i
        cur.pop()

        self.find_all_combinations(arr,res,cur,target,i+1) #Not picking the element but increasing i
        
    
    
    def combinationSum(self, arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res =[]
        self.find_all_combinations(arr,res,[],target,0)
        return res