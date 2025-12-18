class Solution:
    def bfs(self, adj):
        # code here
        
        no_of_nodes = len(adj)
        
        queue = []
        visited = [False for i in range(no_of_nodes) ]
        
        res = []
        
        visited[0] = True
        queue.append(0)
        
        while(len(queue)!=0):
            cur_ele = queue.pop(0)
            res.append(cur_ele)
            
            for node in adj[cur_ele]:
                
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
        
        return res