class Solution:
    
    def dfs(self,node,adj_list,visited,stack):
        for adj_node in adj_list[node]:
            # We visit all the adj node of this particular node
            if not visited[adj_node]:
                visited[adj_node] = True
                self.dfs(adj_node,adj_list,visited,stack)
        
        #print("//--",node)
        # Once all are explored 
        stack.append(node) # we push that element to the stack
        
    
    def topoSort(self, V, edges):
        # Code here
        
        adj_list = [[] for i in range(V)]    
        visited = [False for i in range(V)]
        stack = []
        
        # construct the adj_list
        for edge in edges:
            x,y = edge
            adj_list[x].append(y)

        #print("adj_list",adj_list)
        
        for v in range(0,V):
            if not visited[v]:
                visited[v]=True
                self.dfs(v,adj_list,visited,stack)
        
        res = []
        #print("...stack",stack)
        # Pop the elements from the stack
        for i in range(V-1,-1,-1):
            res.append(stack[i])
        
        #print(".....",res)
        
        return res
        
        