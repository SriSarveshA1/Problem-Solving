#User function Template for python3
class Solution:
    
    def return_count_of_all_subsets_match_target(self,arr,i, target,dp):
        
     
    
        if i==0:
            if arr[0] == 0 and target == 0:
                return 2
            
            if target == 0:
                return 1
            
            if arr[0] == target:
                return 1
            
            
            return 0
        
        
        if dp[i][target] != -1:
            return dp[i][target]
        
        
        not_pick = self.return_count_of_all_subsets_match_target(arr,i-1,target,dp)
        
        pick = 0
        if target-arr[i]>=0:
            pick = self.return_count_of_all_subsets_match_target(arr,i-1,target-arr[i],dp)
        
        dp[i][target] = pick + not_pick
        
        return dp[i][target]
        
        
    
	def perfectSum(self, arr, target):
		# code here
		
		n = len(arr)
		
		dp = [[-1 for j in range(target+1)] for i in range(n)]
		
		return self.return_count_of_all_subsets_match_target(arr,n-1,target,dp)
		
		