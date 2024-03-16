#User function Template for python3

class Solution:
    
    def gcd(self,a,b):

        divisor = min(a,b)
        divident = max(a,b)

        while True:
            if divident%divisor == 0:
                return divisor
            if divident%divisor == 1:
                return 1


            reminder = divident%divisor
            divident = divisor
            divisor = reminder
            
    
    def lcm(self,a,b):
        return int(((a*b)//self.gcd(a,b)))
            
    def lcmAndGcd(self, A , B):
        # code here 
        return [self.lcm(A,B),self.gcd(A,B)]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends