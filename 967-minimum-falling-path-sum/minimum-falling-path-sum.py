class Solution:
    def is_not_valid_i_or_j(self,i,j,m,n):
        if i<0 or i>m-1:
            return True
        
        if j<0 or j>n-1:
            return True
        
        return False

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return min(matrix[0]) # minimum of this row as there is only 1 way to reach this row

        dp = [ [ 0 for j in range(n)] for i in range(m)]

        # Fill the values of the dp[0]th row
        for j in range(n):
            dp[0][j] = matrix[0][j]
        

        for i in range(1,m):
            for j in range(0,n):

                ans1 = 10000000
                ans2 = 10000000
                ans3 = 10000000

                if not self.is_not_valid_i_or_j(i-1,j-1,m,n):# (i-1,j-1)
                    ans1 = dp[i-1][j-1]
                
                if not self.is_not_valid_i_or_j(i-1,j,m,m): #(i-1,j)
                    ans2 = dp[i-1][j]
                
                if not self.is_not_valid_i_or_j(i-1,j+1,m,n): #(i-1,j+1)
                    ans3 = dp[i-1][j+1]
                

                dp[i][j] = min(ans1,ans2,ans3)+matrix[i][j]
            
        
        return min(dp[m-1])
                
        


        