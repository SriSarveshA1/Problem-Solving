class Solution:
    def bfs(self,adj_list,indegree,queue,res):
        
        while(len(queue)!=0):
            node = queue.pop(0)
            res.append(node)
            
            for adj_node in adj_list[node]:
                indegree[adj_node]-=1
                
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
            
        
        
        
                
                
    
    def topoSort(self, V, edges):
        # Code here
        
        adj_list = [[] for i in range(V)]    
        indegree = [0 for i in range(V)]
        res = []
        queue = []
        
        # construct the adj_list
        # Along with that we also construct the indegree
        for edge in edges:
            x,y = edge
            adj_list[x].append(y)
            indegree[y]+=1
            
        
        #1.Then we iterate all the nodes in the indegree and put the nodes which has 0 indegree 
        #into the queue
        for node in range(0,V):
            if indegree[node] == 0:
                queue.append(node)
        
        
        #2.Then seperately we pop from queue(and add it to result set) ,and reduce the indegree of all the adj nodes of that
        # particular nodes, and if any adj_node's indegree becomes 0 we add it to the queue
        
        #3. We continue this until queue becomes empty
        self.bfs(adj_list,indegree,queue,res)
        return res
        
        
        
        

        return res
        
        