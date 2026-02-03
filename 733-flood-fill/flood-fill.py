class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # initial color = image[sr][sc]
        
        # We do bfs from (sr,sc) and add the nodes to the queue whose value is equal to initial color(we can use this
        # as the visiting array alternative)

        # While visiting the node we mark it as color value

        initial_color = image[sr][sc]

        queue = []

        image[sr][sc] = color # marked the initial node as visited
        queue.append((sr,sc))


        m = len(image)
        n = len(image[0])

        visited = [[False for j in range(n)] for i in range(m)]

        while(len(queue)!=0):
            i,j = queue.pop(0)

            # Now iterate the adj nodes of this (i,j)

            # (i+1,j)
            if i+1<=m-1:
                if not visited[i+1][j] and  image[i+1][j] == initial_color: #We can consider this as unvisited logic and add it to bfs
                    queue.append((i+1,j))
                    image[i+1][j] = color # Its like marking it as visited
                    visited[i+1][j] = True

            # (i-1,j)
            if i-1>=0:
                if not visited[i-1][j] and image[i-1][j] == initial_color:
                    queue.append((i-1,j))
                    image[i-1][j] = color
                    visited[i-1][j] = True

            # (i,j+1)
            if j+1<=n-1:
                if not visited[i][j+1] and image[i][j+1] == initial_color:
                    queue.append((i,j+1))
                    image[i][j+1] = color
                    visited[i][j+1]=True

            # (i,j-1)
            if j-1>=0:
                if not visited[i][j-1] and image[i][j-1] == initial_color:
                    queue.append((i,j-1))
                    image[i][j-1] = color
                    visited[i][j-1]=True
        
        return image
            