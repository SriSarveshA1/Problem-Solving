#User function Template for python3

class Solution:
    def exactlyK(self, arr, k):
        # Code here
        
        freq_map = dict()
        
        n = len(arr)
        
        count_of_sub_less_or_equal_to_k = 0
        count_of_sub_less_to_k = 0
        
        i = 0 
        j = 0 
        
        while j<n:
            
            if arr[j] not in freq_map:
                freq_map[arr[j]] =1
            else:
                freq_map[arr[j]] +=1
            
            
            while(len(freq_map) > k):
                
                freq_map[arr[i]]-=1
                
                if freq_map[arr[i]] == 0:
                    del freq_map[arr[i]]
                
                i+=1
                
            if len(freq_map) <= k:
                count_of_sub_less_or_equal_to_k += (j-i+1)
            
            j+=1
        
        #print("count_of_sub_less_or_equal_to_k = ",count_of_sub_less_or_equal_to_k)
        
        i = 0
        j = 0
        
        freq_map = dict()
        
        while j<n:
            
            if arr[j] not in freq_map:
                freq_map[arr[j]] =1
            else:
                freq_map[arr[j]] +=1
            
            
            while(len(freq_map) >= k):
                
                freq_map[arr[i]]-=1
                
                if freq_map[arr[i]] == 0:
                    del freq_map[arr[i]]
                    
                i+=1
                
            if len(freq_map) < k:
                count_of_sub_less_to_k += (j-i+1)
            j+=1
        
        #print("count_of_sub_less_to_k...",count_of_sub_less_to_k)
    
        return count_of_sub_less_or_equal_to_k-count_of_sub_less_to_k
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.exactlyK(arr, k))
        print("~")

# } Driver Code Ends