class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [ [0 for j in range(n)] for i in range(m) ]

        dp[0][0] = 1

        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    continue
                
                ans1 = 0 # [i-1][j]
                ans2 = 0 # [i][j-1]

                if i-1 >= 0:
                    ans1 = dp[i-1][j]
                
                if j-1 >=0:
                    ans2 = dp[i][j-1]
                
                dp[i][j] = ans1+ans2

        
        return dp[m-1][n-1]
