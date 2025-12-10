class Solution(object):

    def find_uniq_paths(self,i,j,m,n):
        if (i >= m ) or (j>=n):
            return 0

        if (i == m-1) and (j == n-1):
            return 1

        ans1 = self.find_uniq_paths(i+1,j,m,n)
        ans2 = self.find_uniq_paths(i,j+1,m,n)
        return ans1+ans2

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[-1 for i in range(n)] for j in range(m)]

        dp[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j==0:
                    continue

                sum1 = 0
                sum2 = 0

                if j-1>=(0):
                    sum1 = dp[i][j-1]
                
                if i-1>=(0):
                    sum2 = dp[i-1][j]

                dp[i][j] = sum1 + sum2
        
        print(dp)
        return dp[m-1][n-1]