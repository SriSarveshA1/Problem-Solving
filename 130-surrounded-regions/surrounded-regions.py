class Solution:
    def return_adj_nodes(self,node,board,m,n):
        # Node will be tuple of (i,j)
        i,j = node

        adj_nodes = []

        if i-1>=0:
            adj_nodes.append((i-1,j))
        
        if i+1<=m-1:
            adj_nodes.append((i+1,j))
        
        if j-1>=0:
            adj_nodes.append((i,j-1))
        
        if j+1<=n-1:
            adj_nodes.append((i,j+1))
        
        return adj_nodes

    def check_if_i_and_j_is_in_border(self,i,j,m,n):
        if i == 0 or i==m-1 or j==0 or j==n-1:
            return True
        
        return False


    def dfs(self,node,board,visited,m,n):
        # From the given node 
        # Get all the adj_node's of the node iterate those nodes which has value as 'o' only

        adj_nodes = self.return_adj_nodes(node,board,m,n)

        for adj_node in adj_nodes:
            i,j = adj_node
            if visited[i][j] == False:
                visited[i][j] = True
                self.dfs(adj_node,board,visited,m,n)



    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. Create a seperate visited matrix and mark all the nodes with 'x' as visited = true
        # 2. ANd mark all '0' as visited =False.
        # 3. Start dfs from all the nodes which are visisted = False and they should be in border , 
        # if yes we start dfs from that node and go to all non-visted node and mark them visited as true
        # 4. Then we again iterate the matrix and mark all the nodes which are not-visisted and mark it as 'x' 

        m = len(board)
        n = len(board[0])

        visited = [ [True if board[i][j]=='X' else False for j in range(n)] for i in range(m)]


        for i in range(0,m):
            for j in range(0,n):
                if visited[i][j] == False and self.check_if_i_and_j_is_in_border(i,j,m,n):
                    visited[i][j] = True
                    self.dfs((i,j),board,visited,m,n)
        

        for i in range(0,m):
            for j in range(0,n):
                if visited[i][j] == False:
                    board[i][j] = 'X'

        return board
        