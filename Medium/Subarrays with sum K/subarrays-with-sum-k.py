#User function Template for python3

class Solution:
    def findSubArraySum(self, arr, N, k):
        # code here
        
        prefix_array = [ 0 for i in range(0,N)]
        
        hash_map = dict()
        
        count = 0
        
        prefix_array[0] = arr[0]
        for i in range(0,N):
            
            if i == 0:
                prefix_array[i] = arr[0]
            else:
                prefix_array[i] = prefix_array[i-1] + arr[i]
            
            

            if (prefix_array[i] - k ) in hash_map:
                count = count + hash_map[(prefix_array[i] - k )]
            
            if (prefix_array[i] == k):
                count = count+1
            
            
            if (prefix_array[i]) in hash_map:
                hash_map[prefix_array[i]] = hash_map[prefix_array[i]] + 1
            
            else:
                hash_map[prefix_array[i]] = 1
                
        return count
            
            
            
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends