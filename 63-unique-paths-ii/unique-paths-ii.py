class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [ [0 for i in range(n)] for j in range(m)]

        dp[0][0] = 0
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j==0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                
                sum1 = 0
                sum2 = 0

                if i-1>=0:
                    sum1 = dp[i-1][j]

                if j-1>=0:
                    sum2 = dp[i][j-1]

                dp[i][j] = sum1+sum2
            
        return dp[m-1][n-1]
            



