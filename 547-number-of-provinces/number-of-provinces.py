class Solution:
    def dfs(self,node,adj_list,visited):
        
        # iterate all the adj nodes of this node
        for i in range(0,len(adj_list[node])):
            # i is adj_node if adj_list[node][i] is 1
            if adj_list[node][i] == 0:
                continue
            
            adj_node = i

            if visited[adj_node]==False:
                visited[adj_node]=True
                self.dfs(adj_node,adj_list,visited)
        
 

    def findCircleNum(self, matrix: List[List[int]]) -> int:

        v = len(matrix)
        
        visited = [False for i in range(v)]

        count = 0

        for node in range(v):

            if visited[node] == False:
                count+=1
                visited[node] = True
                self.dfs(node,matrix,visited)

        return count


        