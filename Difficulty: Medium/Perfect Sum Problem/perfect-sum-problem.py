#User function Template for python3
class Solution:
    
    def return_count_of_all_subsets_match_target(self,arr,i, target,dp):
        if i<0:
            if target == 0:
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
		
		dp = [[0 for j in range(target+1)] for i in range(n)]
		
		if arr[0] == 0:
		    # If the 0th element is 0, so the subsets formed using until idx 0 can be {},{0} total 2
		    dp[0][0] = 2 
		else:
		    # If the 0th element is not 0, then subsets formed using until idx 0 can be {}
		    dp[0][0] = 1
		
		for j in range(1,target+1):
		    # This is filling only until index 0, which means picking elements until 0th index only
		    if arr[0] == j:
		        # This is like elements picking until 0th index and trying to form the jth (target value)
		        dp[0][j] = 1
		
		for i in range(1,n):
		    for j in range(0,target+1):
		        
		        not_pick = dp[i-1][j]
		        
		        pick = 0
		        if j-arr[i]>=0:
		            pick = dp[i-1][j-arr[i]]
		           
		        dp[i][j] = pick+not_pick
		 
		return dp[n-1][target]
		        
		        
		        
		        
		        
		
		
		