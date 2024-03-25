#User function Template for python3
import math

class Solution:
    
    
    
    def power (self, a, N):
        #complete the function here
        if (N == 1):
            return a
            
        if (N == 0):
            return 1
        
        if ( (N % 2) == 0):
            
            ans = self.power(a, math.floor(N/2))
            return (ans*ans) % 1000000007
        else:
            
            ans = self.power(a, math.floor(N/2)) 
            return (ans*ans*a) % 1000000007
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a, b = map(int,input().split())
        ob = Solution()
        print(ob.power(a, b))
# } Driver Code Ends