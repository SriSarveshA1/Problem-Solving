#User function Template for python3
import math

class Solution:
	def setBit(self, N):
		# code here
	    total_no_actual_bits = math.ceil(math.log2(N))
	    
	    mask = 1
	    
	    while(total_no_actual_bits>0):
	        
	        if N & mask == 0:
	            return N|mask
	        
	        mask = mask<<1
	        
	        total_no_actual_bits-=1

        return N
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())

		ob = Solution()
		ans = ob.setBit(N)
		print(ans)




# } Driver Code Ends