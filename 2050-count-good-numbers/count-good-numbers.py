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

        no_of_even = None
        no_of_odd = None
        
        if n%2 == 0:
            # even
            print("in even")
            no_of_even = math.ceil((n-1)/2)
            print("///event",no_of_even)
            no_of_odd = n - no_of_even
            print("///no of odd",no_of_odd)
        else:
            print("in odd")
            no_of_even = math.ceil(n/2)
            no_of_odd = n - no_of_even
        
        print("no_of_even = ",no_of_even)
        print("no_of_odd = ",no_of_odd)

        if (n%2)!=0:
            return (self.temp(5,no_of_even) * self.temp(4,no_of_odd)) % mod
        else:
            return (self.temp(5,no_of_even) * self.temp(4,no_of_even)) % mod