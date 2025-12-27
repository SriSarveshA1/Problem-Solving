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

        max_v = 100000000

        dp = [max_v for j in range(0,len(triangle[m-1]))]

        dp[0] = triangle[0][0]

    
        for i in range(1,m):
            for j in range((len(triangle[i])-1) , -1, -1 ): # starting from the end_idx, step=-1,goes till end

                ans1 = 100000000 # (i-1,j-1)
                ans2 = 100000000 # (i-1,j)

                if self.check_for_valid_i_and_j(triangle,i-1,j-1):
                    ans1 = dp[j-1]
                
                if self.check_for_valid_i_and_j(triangle,i-1,j):
                    ans2 = dp[j]
                
                dp[j] = min(ans1,ans2) + triangle[i][j]
               # print("dp" , dp)
        
        
        
        return min(dp)



        