class Solution:
    def return_adj_row_cols_pairs(self,mat,m,n,i,j):
        # For the particular (i,j) return the adj nodes in all the 4 directions
        # (i+1,j)
        # (i-1,j)
        # (i,j-1)
        # (i,j+1)

        adj_nodes = []
        if (i+1)<=m-1:
            adj_nodes.append((i+1,j))
        
        if (i-1)>=0:
            adj_nodes.append((i-1,j))
        
        if (j-1)>=0:
            adj_nodes.append((i,j-1))
        
        if (j+1)<=n-1:
            adj_nodes.append((i,j+1))

        return adj_nodes

    def bfs(self,queue,mat,m,n,visited,levels,i,j):
        # Now we will do bfs for each of the nodes starting from (i,j)
        # 1. Mark all the adj nodes of (i,j) as visited as True
        # 2. And also compute the levels of all the adj nodes starting from (i,j) and while setting the value of a level of adj_row,adj_col
        # we check if the new level is lesser than what already set or else we don't change anything

        while(len(queue)!=0):
            node = queue.pop(0)

            # Iterate all the adj_nodes of node
            adj_nodes = self.return_adj_row_cols_pairs(mat,m,n,node[0],node[1])

            for adj_node in adj_nodes:
                if not visited[adj_node[0]][adj_node[1]] and mat[adj_node[0]][adj_node[1]] == 1:
                    visited[adj_node[0]][adj_node[1]] = True
                    # Since this particular node is not visited try to compute the level of this adj_node[0],adj_node[1] from the node[0],node[1]
                    computed_level = levels[node[0]][node[1]]+1
                    if computed_level < levels[adj_node[0]][adj_node[1]]:
                        levels[adj_node[0]][adj_node[1]] = computed_level

                    queue.append((adj_node[0],adj_node[1]))
                            
        

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # We will have visited matrix[][] where each of the i,j tell's whether this particular (i,j) is visited or not
        # And also level's matrix[][] where each of the i,j tell whats the shortest level from some 0th starting node(out of 
        # all the starting 0th nodes)

        m = len(mat)
        n = len(mat[0])

        max_level = 10000000
        
        visited = [[False for j in range(n)] for i in range(m) ]
        levels = [[max_level for j in range(n)] for i in range(m)]


        queue = []

        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j] == 0:
                    levels[i][j] = 0
                    visited[i][j] = True
                    queue.append((i,j))
        
        self.bfs(queue,mat,m,n,visited,levels,i,j)

        return levels

