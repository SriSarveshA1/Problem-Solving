class Solution:
    def minCost(self, arr):
        n = len(arr)
        
        if n==1:
            return 0
        
        if n==2:
            return abs(arr[1]-arr[0])
        
        # code here
        dp = [0 for i in range(n)]
        
        dp[0] = 0
        dp[1] = abs(arr[1]-arr[0])
        
        for i in range(2,n):
            ans1 = dp[i-1] + abs(arr[i]-arr[i-1])
            ans2 = dp[i-2] + abs(arr[i]-arr[i-2])
            
            dp[i] = min(ans1,ans2)
        
        return dp[n-1]