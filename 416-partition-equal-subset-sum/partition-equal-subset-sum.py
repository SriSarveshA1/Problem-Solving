class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        # code here 
        target = 0
        for ele in arr:
            target += ele
        
        if target%2!=0:
            return False

        target = target // 2

        n = len(arr)
        dp = [[False for j in range(0,target+1)] for i in range(n)]

        # i-> 0 to n represents the index in arr,
        # j -> 0 to target represent all the values between 0 to target
        # Basically the values between j -> 0 represents the target values
        
        for i in range(0,n):
            for j in range(0,1):
                # Only the first column alone all the values will be True,
                # Because its like using the elements from [0 to i] are we able to achieve the target or not
                dp[i][j] = True
                # This will be True for the first column only because, just by not picking any element
                # within 0 to i we can reach the target 0.
            
  
        for i in range(0,1):
        # And as per the base case when i == 0, when we are at the first row
        # its like if the particular i=0 th index value in the arr is matching with target(j) then it will be True 
        # else False
            for j in range(0,target+1):
                if arr[i] == j:
                    dp[i][j] = True
        
        
        # We start from the 2nd row and try to compute for each i,j
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
        
        for i in range(1,n):
            for j in range(1,target+1):
                
                not_pick = dp[i-1][j]
                pick = False
                if (j-arr[i])>=0:
                    pick= dp[i-1][j-arr[i]]
                
                dp[i][j] = pick or not_pick
        
        return dp[n-1][target]