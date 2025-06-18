import math

class Solution:
    def temp(self,x,N):
        mod = 1000000007

        if N==1:
            return x
        
        if N==0:
            return 1
        

        ans = self.temp(x, math.floor(N/2))

        if (N%2) == 0:    
            return (ans*ans) % mod
        else:
            return (ans*ans*x) % mod

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5 
        
        if n == 2:
            return 20
        
        mod = 1000000007

        no_of_ods = math.floor((n-1)/2)
        no_of_evens = math.ceil(n/2)

        if (n%2)!=0:
            return (self.temp(5,no_of_evens) * self.temp(4,no_of_ods)) % mod
        else:
            return (self.temp(5,no_of_evens) * self.temp(4,no_of_evens)) % mod