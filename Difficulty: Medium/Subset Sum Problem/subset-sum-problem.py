class Solution:
    
    def find_subset_exist(self,n,arr,i,target):
        
        if target <0:
            return False
        
        if i>=n:
            if target == 0:
                return True
            
            return False
        
        pick = self.find_subset_exist(n,arr,i+1,target-arr[i])
        
        not_pick = False
        if not pick:
            not_pick = self.find_subset_exist(n,arr,i+1,target)
        
        return not_pick or pick
        
        
    def isSubsetSum (self, arr, target):
        # code here 
        
        n = len(arr)
        return self.find_subset_exist(n,arr,0,target)
        
        