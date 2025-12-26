class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [ [0 for j in range(n)] for i in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    continue
                
                ans1 = 1000000
                ans2 = 1000000

                if (i-1) >= 0:
                    ans1 = dp[i-1][j]
                
                if (j-1) >= 0:
                    ans2 = dp[i][j-1]
                
                dp[i][j] = min(ans1,ans2) + grid[i][j]
            
        
        return dp[m-1][n-1]
