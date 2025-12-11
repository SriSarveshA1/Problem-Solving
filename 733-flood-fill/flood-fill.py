class Solution(object):
    
    def modify_image(self,m,n,matrix,start_color,target_color,i,j):
        if i>=m or i<0 or j>=n or j<0:
            return
        
        cur_color = matrix[i][j]


        if cur_color != start_color or cur_color == target_color:
            return
        
        if cur_color == start_color:
            matrix[i][j] = target_color
        
        self.modify_image(m,n,matrix,start_color,target_color,i,j-1)
        self.modify_image(m,n,matrix,start_color,target_color,i,j+1)
        self.modify_image(m,n,matrix,start_color,target_color,i-1,j)
        self.modify_image(m,n,matrix,start_color,target_color,i+1,j)



    def floodFill(self, matrix, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_color = matrix[sr][sc]
        target_color = color

        m = len(matrix)
        n = len(matrix[0])

        self.modify_image(m,n,matrix,start_color,target_color,sr,sc)
        return matrix
        

        


        