class Solution:

    def generate_all_possible_paths(self,board,visited,word,idx,row,col):
        m=len(board)
        n=len(board[0])

        if idx+1 >= len(word):
            # If we reached all the index of the word
            return True

        # For each (row,col) there are 4 possible options 
        # (row,col+1)
        # (row+1,col) , we go in this way if board[row+1,col] == word[idx+1] && visited[row+1,col] is false
        # (row-1,col) , 
        # (row,col-1)

        # when we are here initially we have 

        # (row,col+1)
        if (col+1)<=n-1 and board[row][col+1] == word[idx+1] and not visited[row][col+1]:
            visited[row][col+1] = True
            result = self.generate_all_possible_paths(board,visited,word,idx+1,row,col+1)
            visited[row][col+1] = False
            if result:
                return True
        
        # (row+1,col)
        if (row+1)<=m-1 and board[row+1][col] == word[idx+1] and not visited[row+1][col]:
            visited[row+1][col] = True
            result = self.generate_all_possible_paths(board,visited,word,idx+1,row+1,col)
            visited[row+1][col] = False
            if result:
                return True

        # (row-1,col)
        if (row-1)>=0 and board[row-1][col] == word[idx+1] and not visited[row-1][col]:
            visited[row-1][col] = True
            result = self.generate_all_possible_paths(board,visited,word,idx+1,row-1,col)
            visited[row-1][col] = False
            if result:
                return True
        
        # (row,col-1)
        if (col-1)>=0 and board[row][col-1] == word[idx+1] and not visited[row][col-1]:
            visited[row][col-1] = True
            result = self.generate_all_possible_paths(board,visited,word,idx+1,row,col-1)
            visited[row][col-1] = False
            if result:
                return True


        return False            


    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [ [False for j in range(n)] for i in range(m)]

        # Iterate of each of the cell in the board where ever board[i][j] == word[0], we start the recursive calls 
        # from there
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # start the backtracking
                    #mark the i,j as visited
                    visited[i][j]=True
                    result = self.generate_all_possible_paths(board,visited,word,0,i,j)
                    visited[i][j]=False
                    # At some point if the result(of backtracking) returns true we return True from here
                    if result:
                        return True
        return False

