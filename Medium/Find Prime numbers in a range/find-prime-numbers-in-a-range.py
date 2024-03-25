#User function Template for python3

class Solution:   
    def sieveOfEratosthenes(self,M, N):
        #code here 
        
        prime_arrays = [ True for i in range(0,N+1)]
        
        prime_arrays[0] = False
        prime_arrays[1] = False
        
        for i in range(2,int(math.sqrt(N))+1):
            
            if prime_arrays[i] == True:
                
                starting_multiple = i*i  # starting to iterate from the i*i and 
                
                while(starting_multiple<=N): # and going to find all of its multiples <=N
                    prime_arrays[starting_multiple] = False
                    starting_multiple = starting_multiple+i
            
        result = []
        for i in range(M,N+1):
            if prime_arrays[i] == True:
                result.append(i)
        
        return result
        
    def primeRange(self,M,N):
        #code here
        
        return self.sieveOfEratosthenes(M,N)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends