class Solution:
    def check_for_valid_i_and_j(self,triangle,i,j):
        m = len(triangle)

        if (i<0 or i>m-1):
            return False
        
        n = len(triangle[i])

        if (j<0 or j>n-1):
            return False
        
        return True


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        if m == 1:
            return triangle[0][0]

        dp = []

        # iterate 
        for row in range(0,m):
            col_length = len(triangle[row]) # finding the column length for each row
         
            dp.append([0 for k in range(0,col_length)]) # creating an array of that length and appending
        
        dp[0][0] = triangle[0][0]

    
        for i in range(1,m):
            for j in range(0,len(triangle[i])):
                ans1 = 100000000 # (i-1,j-1)
                ans2 = 100000000 # (i-1,j)

                if self.check_for_valid_i_and_j(triangle,i-1,j-1):
                    ans1 = dp[i-1][j-1]
                
                if self.check_for_valid_i_and_j(triangle,i-1,j):
                    ans2 = dp[i-1][j]
                
                dp[i][j] = min(ans1,ans2) + triangle[i][j]
        
        
        return min(dp[m-1])



        