class Solution:
    
    def dfs(self,node,adj_list,visited,cur):
        cur.append(node)
        
        # iterate all the adj nodes of this node
        for adj_node in adj_list[node]:
            if visited[adj_node]==False:
                visited[adj_node]=True
                self.dfs(adj_node,adj_list,visited,cur)
        
        
    
    
    def getComponents(self, v, edges):
        # code here
        
        # 1.Construct the adj list
        
        adj_list = [[] for i in range(v) ]
        
        no_edges = len(edges)
        
        for edge in edges:
            x = edge[0]
            y = edge[1]
            
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        #print('..',adj_list)
        
        visited = [False for i in range(v)]
    
        res = []
            
        for node in range(v):
            # If this particular node is not visited we try dfs for it
            if visited[node] == False:
                cur = []
                visited[node] = True
                self.dfs(node,adj_list,visited,cur)
                res.append(cur)
        
        return res
            