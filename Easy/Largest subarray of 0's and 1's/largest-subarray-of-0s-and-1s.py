#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        prefix_sum = [ 0 for i in range(0,N) ]
        hash_map = dict()
        
        if arr[0] == 0:
            prefix_sum[0] = -1
        else:
            prefix_sum[0] = 1
            
        
        for i in range(1,N):
            
            val = arr[i]
            
            if(val == 0):
                val = -1
            
            cur_sum = prefix_sum[i-1]+val
            
            prefix_sum[i] = cur_sum
        
        max_length = 0
        
        for i in range(0,N):
            
            if prefix_sum[i] == 0:
                max_length = max(max_length,i+1)
                continue
            
            if prefix_sum[i] not in hash_map:
                hash_map[prefix_sum[i]] = i
            else:
                 max_length = max(max_length,i-hash_map[prefix_sum[i]])
        
            # if cur_sum not in hash_map:
            #     hash_map[cur_sum] = i
            # else:
            #     if cur_sum == 0:
            #         max_length = max(max_length,(i+1))
            #     else:
            #         max_length = max(max_length,(i - hash_map[cur_sum]))
            
            
        #print(prefix_sum)
        return max_length
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends