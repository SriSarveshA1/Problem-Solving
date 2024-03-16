#User function Template for python3
import math

class Solution:
	def AllPrimeFactors(self, N):
		# Code here
		unique_pf = []
		
		n = N
		
		if n==1:
		    return []
		
		for i in range(2,math.floor(math.sqrt(n)+1)):
		    
		    if n%i == 0:
		        unique_pf.append(i)
		       
		    while((n%i)==0):
		        n = int(n/i)
    
        if n>1: # its a number which doesn't have the factors from 2 to sqrt(n) so its a prime
            unique_pf.append(n)
        
        return unique_pf
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends