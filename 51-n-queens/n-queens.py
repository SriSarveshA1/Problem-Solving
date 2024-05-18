class Solution(object):
    def check(self,mat,i,j):
        n = len(mat)
        # left diagonal
        temp_i = i
        temp_j = j

        while(temp_i>=0 and temp_j>=0):
            if(mat[temp_i][temp_j]=='Q'):
                return False
            temp_i-=1       
            temp_j-=1
        
        # top column
        temp_i = i
        temp_j = j

        while(temp_i>=0 and temp_j>=0):
            if(mat[temp_i][temp_j]=='Q'):
                return False
            temp_i-=1       
        
        # right diagonal
        temp_i = i
        temp_j = j
        
        while(temp_i>=0 and temp_j>=0 and temp_j<n):
            if(mat[temp_i][temp_j]=='Q'):
                return False
            temp_i-=1       
            temp_j+=1
        
        return True


    def temp(self,result,placed_queens,mat,n,i):
       
        
        if placed_queens == n:
            cur = []
            for row in range(0,n):
                s = ""
                for col in range(0,n):
                    s+=mat[row][col]

                cur.append(s)
            
            result.append(cur)
            return
        
        if i>=n:
            return
        
        for j in range(0,n):
            #print("i  = ",i ," j = ",j)
            if self.check(mat,i,j):
                mat[i][j] = 'Q'
                placed_queens+=1
                
                self.temp(result,placed_queens,mat,n,i+1)
                #print(mat)
                placed_queens-=1
                mat[i][j] = '.'
    
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        mat = []
        for i in range(0,n):
            cur = []
            for j in range(0,n):
                cur.append('.')
            mat.append(cur)

        print("mat = ",mat)

        result = []
        placed_queens = 0
        self.temp(result,placed_queens,mat,n,0)
        return result