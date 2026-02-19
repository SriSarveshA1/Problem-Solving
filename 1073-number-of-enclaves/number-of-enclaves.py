class Solution:

    def is_boundary(self,i,j,m,n):

        if i==0 or i == m-1 or j == 0 or j == n-1:
            return True
        
        return False

    def return_adj_nodes(self,node,grid):
        i,j = node

        adj_nodes = []
        m = len(grid)
        n = len(grid[0])

        if i-1 >=0:
            adj_nodes.append((i-1,j))
        
        if i+1 <=m-1:
            adj_nodes.append((i+1,j))
        
        if j-1 >= 0:
            adj_nodes.append((i,j-1))
        
        if j+1 <=n-1:
            adj_nodes.append((i,j+1))
        
        return adj_nodes


    def dfs(self,node,grid,visited):
        adj_nodes = self.return_adj_nodes(node,grid)

        for adj_node in adj_nodes:
            i,j = adj_node
            if visited[i][j] == False and grid[i][j] == 1:
                visited[i][j] =True
                self.dfs(adj_node,grid,visited)


    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Have a visited array of m,n and mark the elements which is of 0 as Visited[i][j]=True, the node with value 1 as visited[i][j]=False
        # And we do dfs on all the nodes which are not visisted and they are on the boundary
        # while doing dfs we mark a particular cell as visisted[i][j] = True if we were able to reach that node during dfs
        # Finally we iterate the grid and count the nodes which are not visisted and return the count

        m = len(grid)
        n = len(grid[0])

        visited = [[ True if grid[i][j] == 0 else False for j in range(n)] for i in range(m)]

        for i in range(0,m):
            for j in range(0,n):
                if visited[i][j] == False and self.is_boundary(i,j,m,n):
                    visited[i][j] = True
                    self.dfs((i,j),grid,visited)
        
        count = 0
        for i in range(0,m):
            for j in range(0,n):
                if visited[i][j] == False:
                    count+=1
        
        return count


