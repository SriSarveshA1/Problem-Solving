#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, N):
        #code here 
        
        prime_arrays = [ True for i in range(0,N+1)]
        
        
        for i in range(2,int(math.sqrt(N))+1):
            
            if prime_arrays[i] == True:
                
                starting_multiple = i*i  # starting to iterate from the i*i and 
                
                while(starting_multiple<=N): # and going to find all of its multiples <=N
                    prime_arrays[starting_multiple] = False
                    starting_multiple = starting_multiple+i
            
        result = []
        for i in range(2,N+1):
            if prime_arrays[i] == True:
                result.append(i)
        
        return result
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends