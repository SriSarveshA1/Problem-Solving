#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefix_sum = [0 for i in range(0,n)]
        prefix_sum[0] = arr[0]
        for i in range(1,n):
            prefix_sum[i] = (prefix_sum[i-1]+arr[i])
        
        #print("prefix_sum....",prefix_sum)
        
        first_occurence = dict()
        
        max_length = 0
        
        for i in range(0,n):
            
            
            if prefix_sum[i] == 0:
                max_length = max(max_length, i+1)
            else:
                if prefix_sum[i] in first_occurence:
                    # check whether the prefix[r] already occured in the previous index's
                    # which means there is prefix[l] == prefix[r] where l occured previously
                    
                    
                    # so the first_occurence[prefix_sum[i]]  gives the sum from 0 to (l-1)
                    
                    length = ( i - first_occurence[prefix_sum[i]] ) # will give the subarray of  length between (l) to r
                    
                    
            
                    max_length = max(max_length , length )
                else:
                    first_occurence[prefix_sum[i]] = i 
        
        return max_length
        
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends