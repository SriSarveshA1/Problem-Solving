#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        
        n = len(height)
        
        if n==1:
            return 0
        
        if n==2:
            return abs(height[1]-height[0])
        
        dp = [0 for i in range(n)]
        
        dp[0] = 0
        dp[1] = abs(height[1]-height[0])
        
        for i in range(2,n):
            dp[i] = min (
                dp[i-2]+abs(arr[i]-arr[i-2]),
                dp[i-1]+abs(arr[i]-arr[i-1])
                )
        
        return dp[n-1]
        