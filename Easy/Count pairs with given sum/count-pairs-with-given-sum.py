#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        freq = dict()
        
        pairs = 0
        
        for ele in arr:
            
            if (k-ele) in freq:
                pairs += freq[k-ele]
            
            if ele in freq:
                freq[ele] = freq[ele]+1
            else:
                freq[ele] = 1
                
        return pairs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends