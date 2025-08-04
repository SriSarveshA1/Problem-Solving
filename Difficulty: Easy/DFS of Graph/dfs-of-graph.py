class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    
    def helper(self,adj,source_node,result,visited):
        
        result.append(source_node)
        
        
        for adj_node in adj[source_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                self.helper(adj,adj_node,result,visited)
        
    
    
    def dfs(self, adj):
        # code here
        n = len(adj)
        
        result = []
        visited = [False for i in range(n)]
        
        visited[0] = True
        self.helper(adj,0,result,visited)
        return result
        
        