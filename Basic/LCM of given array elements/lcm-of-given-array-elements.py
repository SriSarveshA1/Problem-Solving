#User function Template for python3
class Solution:
    
    def gcd(self,a,b):
        divisor = min(a,b)
        divident = max(a,b)
        
        while True:
            if divident % divisor == 0 :
                return divisor
                
            if divident % divisor == 1:
                return 1
            
            reminder = divident % divisor
            divident = divisor
            divisor = reminder
            
    def lcm(self,a,b):
        gcd_a_b = self.gcd(a,b)
        lcm = (a*b) / gcd_a_b
        return int(lcm)
    
    def lcmOfArray(self, N, A):
        # code here
        if(len(A)==1):
            return A[0]
            
        ans = self.lcm(A[0],A[1]) % 1000000007
        
        for i in range(2,len(A)):
            ans = self.lcm(ans,A[i]) % 1000000007
        
        return ans        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		A = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.lcmOfArray(N,A)
		print(ans)
# } Driver Code Ends