import heapq

class Solution:

    def mergeArrays(self, mat):
        # Code here
        
        pq = []
        
        res = []
        
        m = len(mat)
        n = len(mat[0])
        
        k = m
        
        # Now we try to enter the first k elements , from the first column 
        # as the first column consists of the least elements amoung the entire matrix
        # and out of all the elements of the column ,after inserting the elements into the heap
        # the first element that we are going to pop() will be the smallest of all.
        
        for i in range(0,m):
            # Same first column, and we are iterating all the rows of that column
            heapq.heappush(pq,(mat[i][0],i,0))
        
        # So until now we have all the possible candidates for the 0th element of the overall result
        
        while len(pq) != 0:
            # Now if we pop the elements from heap and start to insert into the final res
            
            value, i, j = heapq.heappop(pq) # The value that we popped is the smallest element among the 
            # other possible values in the heap and that is the most eligible value to be inserted at
            # this point of time
            
            res.append(value)
            
            # after we popped an element from the heap, then the next possible value
            # can be lying either in the next element of the popped element's array
            # or , it can be already within the elements of the heap
            
            # so we should insert the next set of elements from the row of the element which is popped as 
            # it can have the next element that can be part of the result
            
            if j+1 < n: # checking if there any elements left to insert in that particular row
                heapq.heappush(pq,(mat[i][j+1],i,j+1))
            
        
        return res
                
            
            
            
            
        
        