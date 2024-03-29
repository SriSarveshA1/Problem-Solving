class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    
    
    def maxDistance(self, arr, n):
        # Code here
        
        elem_with_index = dict()
        
        max_diff = -1
        
        for i in range(0,n):
            
            if arr[i] not in elem_with_index:
                elem_with_index[arr[i]] = i
                max_diff = max( max_diff, 0 )
            else:
                cur_diff = i - elem_with_index[arr[i]]
                max_diff = max( max_diff, cur_diff )
            
        return max_diff


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends