class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        n = len(adj)
        
        visited = [False for i in range(n)]
        
        queue = [0]
        visited[0] = True

        res = []
        
        while True:
            
            current_node = queue.pop(0)
            
            res.append(current_node) 
            
            for adj_node in adj[current_node]:
                if not visited[adj_node]:
                    queue.append(adj_node) 
                    visited[adj_node] = True # We should mark this node visited as soon as possible
                    # because the next node we might visit can also have the same adj_node as its adjasent
                    # if we mark this now only as visited the next node won't be markthing this adj
            
            if not queue:  # Replace 'condition' with your actual loop condition
                break
               
        
        return res
        
        
        
        
        