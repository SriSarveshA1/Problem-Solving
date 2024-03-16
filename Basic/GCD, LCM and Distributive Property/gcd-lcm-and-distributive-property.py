#User function Template for python3

class Solution:
    
    def gcd(self,a,b):
    
        if a==0:
            return b
            
        if b==0:
            return a
            
        divisor = min(a,b)
        divident = max(a,b)
        

        
        while True:
            
            if divident % divisor == 0:
                return divisor
            
            if divident % divisor == 1:
                return 1
            
            
            reminder = divident % divisor
            divident = divisor
            divisor = reminder
        

    def lcm(self,a,b):
        
        lcm = int( (a*b) / self.gcd(a,b) )
        
        return lcm
        
    
    
    def findValue (self, x, y, z):
        #complete the function here
        
        return self.gcd(self.lcm(x,y),self.lcm(x,z))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        x, y, z = map(int,input().split())
        ob = Solution()
        print(ob.findValue(x, y, z))
# } Driver Code Ends